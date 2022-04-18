from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('login', log, name="login"),
    path('logout', user_logout, name="logout"),
    path('register', reg, name="register"),
    path('add_post/', add_post, name="add_post"),
    path('view_comments', view_and_add_comments, name="comments"),

]