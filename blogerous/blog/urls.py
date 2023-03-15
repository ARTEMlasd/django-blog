from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about),
    path('sign-up/', register, name="register-form"),
    path('post/<int:id>/', reading_post, name='post'),
    path('sign-up/true/', register_new_user, name="register-new-user"),
    path('come-in/true/', check_come_in, name="check-come-in"),
    path('come-in/', come_in, name="come_in"),
    path('my/account/', users, name="users"),
    path('save-post/', save_post, name='save-post'),
    path('logout', logout, name='logout'),
    path('likes/<int:User_id>/<int:post_id>/', likes, name='likes'),
    path('comments/<int:post_id>/', comment, name='comment')

]
