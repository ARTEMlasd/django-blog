from django.shortcuts import render, redirect
from .models import Posts, Users, Likes, Comment
from django.http import HttpResponseRedirect
from .forms import AddCommentForm
import random


def index(request):
    if 'auth' in request.COOKIES:
        is_authenticated = True
    else:
        is_authenticated = False
    print(is_authenticated)
    posts = Posts.objects.all()
    return render(request, "blog/index.html", {"posts": posts, "auth": is_authenticated})


def about(response):
    return render(response, 'blog/about.html')


def register(response):
    return render(response, 'blog/regisor.html')


def reading_post(request, id):
    post = Posts.objects.get(id=id)
    post.views += 1
    post.save()
    comments = Comment.objects.filter(post_id=post.pk )

    username = request.COOKIES["auth"]
    user = Users.objects.get(nic=username)
    likes_amount = Likes.objects.filter(post_id=post.pk)
    post_likes = Likes.objects.filter(post_id=post.pk, User_id=user.pk)
    like_status = True if len(post_likes) > 0 else False
    return render(
        request,
        "blog/post.html",
        {
            'comments': comments,
            'likes_amount': len(likes_amount),
            'post': post,
            'user': user,
            'lk': like_status,
            'form': AddCommentForm
        }
    )


def register_new_user(request):
    if request.method == 'POST':
        new_user = Users(name=request.POST['name'], nic=request.POST['login'], mail= request.POST['email'], password= request.POST['password'])
        if request.POST['password'] != request.POST['password2']:
            return render(request, 'blog/regisor.html')
        new_user.save()
    return redirect('come_in')


def come_in(response):
    return render(response, 'blog/index3.html')


def check_come_in(request):
    if request.method == 'POST':
        old_email = request.POST['email']
        old_password = request.POST['password3']
        user = Users.objects.filter(mail=old_email)
        print(user)
        if user[0].password == old_password:
            res = HttpResponseRedirect('/')
            res.set_cookie('auth', user[0].nic)
            return res
        else:
            return render(request, 'blog/index3.html')
    return redirect(index)


def users(response):
    username = response.COOKIES["auth"]
    user = Users.objects.get(nic=username)
    user_posts = Posts.objects.filter(author=user.pk)
    return render(response, 'blog/user.html', {'username': username, 'posts':user_posts})


def save_post(request):
    if request.method == 'POST':
        username = request.COOKIES["auth"]
        user = Users.objects.get(nic=username)
        New_Post = Posts(
            author=user.pk,
            title=request.POST['title'],
            text=request.POST['discription'],
            likes=0,
            comment='Спасибо что создали пост',
            views=0,
            date=0
        )
        New_Post.save()
    return redirect('users')


def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('auth')
    response .delete_cookie('auth')
    return response


def likes(request, User_id, post_id):
    new_like = Likes(
        User_id=User_id,
        post_id=post_id
    )
    new_like.save()
    return redirect("post", id=post_id)


def Views(request, User_id, post_id):
    Views = Views(
        User_id=User_id,
        post_id=post_id
    )
    Views.save()
    return redirect("post", id=post_id)


def comment(request,  post_id):
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        user = Users.objects.get(nic=request.COOKIES["auth"])
        comment = Comment(
            User_id=user.pk,
            post_id=post_id,
            text=form.data['text']
        )
        pass
    comment.save()
    return redirect('post', id=post_id)
