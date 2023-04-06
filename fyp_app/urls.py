from django.urls import path
from .views import login, feedback, home, bbc, cnn, newscategory, espn

urlpatterns = [
    path("", login, name="login"),
    path("home/", home, name="home"),
    path("bbc/", bbc, name="BBC"),
    path("cnn/", cnn, name="CNN"),
    path("newscategory/", newscategory, name="newscategory"),
    path("feedback/", feedback, name="feedback"),
    path("espn/", espn, name="ESPN"),
    # path('home/myhome/', myhome, name = 'myhome'),
]
