from django.urls import path
from .views import (
    login,
    feedback,
    home,
    bbc,
    cnn,
    newscategory,
    espn,
    register,
    index,
    logout_view,
)

urlpatterns = [
    path("", index, name="index"),
    path("home", home, name="home"),
    path("bbc", bbc, name="BBC"),
    path("cnn", cnn, name="CNN"),
    path("newscategory", newscategory, name="newscategory"),
    path("feedback", feedback, name="feedback"),
    path("espn", espn, name="ESPN"),
    # path('home/myhome/', myhome, name = 'myhome'),
    path("register", register, name="register"),
    path("login", login, name="login"),
    path("logout", logout_view, name="logout_view"),
]
