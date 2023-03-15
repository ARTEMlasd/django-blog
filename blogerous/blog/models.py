from django.db import models


class Users(models.Model):
    name = models.TextField(default='None')
    nic = models.TextField(default='None')
    password = models.TextField(default='int')
    mail = models.TextField(default='None')


class Posts(models.Model):
    author = models.IntegerField(default=0)
    title = models.TextField(default='None')
    likes = models.IntegerField()
    comment = models.TextField(default=' ')
    date = models.IntegerField()
    views = models.IntegerField()
    text = models.TextField(default='None')


class Likes(models.Model):
    User_id = models.IntegerField(default=0)
    post_id = models.IntegerField(default=0)


class Comment(models.Model):
    User_id = models.IntegerField(default=0)
    post_id = models.IntegerField(default=0)
    text = models.TextField(default='', max_length=100)
