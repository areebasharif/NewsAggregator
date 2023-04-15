from newsapi import NewsApiClient
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
from .models import Registeration
import requests
from django.contrib.auth.models import User
from django.contrib import messages
import requests
from django.shortcuts import render, redirect
from django.urls import reverse
import speech_recognition as sr
from .forms import NewUserForm, UserLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate 
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def login(request):
    return redirect(reverse("login"))


# Create your views here.
@login_required(login_url="login")
def home(request):
    newsapi = NewsApiClient(api_key="5e712cb029c5432e82fa92a5ec4083b2")
    everything = newsapi.get_everything(sources="al-jazeera-english")
    articles = everything["articles"]
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])

    mylist = zip(news, desc, img)

    return render(request, "home.html", context={"mylist": mylist})


API_KEY = "5e712cb029c5432e82fa92a5ec4083b2"


@login_required(login_url="login")
def newscategory(request):

    articles = None


    if request.POST:
        data = request.POST.dict()
        category = data["transcribed_text"]
        url = f"https://newsapi.org/v2/top-headlines?language=en&category={category}&apiKey={API_KEY}"
        response = requests.get(url)
        resp = response.json()
        articles = resp["articles"]

    context = {"articles": articles}

    return render(request, "newscategory.html", context)


@login_required(login_url="login")
def bbc(request):
    newsapi = NewsApiClient(api_key="5e712cb029c5432e82fa92a5ec4083b2")
    everything = newsapi.get_everything(sources="bbc-news" , language="en")
    articles = everything["articles"]

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])

    mylist = zip(news, desc, img)

    return render(request, "bbc.html", context={"mylist": mylist})



@login_required(login_url="login")
def cnn(request):
    newsapi = NewsApiClient(api_key="5e712cb029c5432e82fa92a5ec4083b2")
    everything = newsapi.get_everything(sources="cnn" , language="en")
    articles = everything["articles"]

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])

    mylist = zip(news, desc, img)

    return render(request, "cnn.html", context={"mylist": mylist})


@login_required(login_url="login")
def espn(request):
    newsapi = NewsApiClient(api_key="5e712cb029c5432e82fa92a5ec4083b2")
    everything = newsapi.get_everything(sources="espn-cric-info", language="en")
    articles = everything["articles"]

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])

    mylist = zip(news, desc, img)

    return render(request, "espn.html", context={"mylist": mylist})


@login_required(login_url="login")
def feedback(request):
    return render(
        request,
        "feedback.html",
    )


def save_form(request):
    if request.method == "POST":
        name = request.POST["name"]
    email = request.POST["email"]
    message = request.POST["message"]
    if len(name) < 2 or len(email) < 3 or len(message) < 4:
        messages.error(request, "Please fill the form correctly")
    else:
        en = Contact(name=name, email=email, message=message)
        en.save()
 
    return render(request, "feedback.html")


def login(request):

    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            print(user, form)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(reverse("home"))
            else:
                print(user)
                messages.error(request, "Invalid username or password.")

    return render(request=request, template_name="login.html", context={"form": form})


def register(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            messages.success(request, "Registration successful.")

            return redirect(reverse("login"))

    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)

    return redirect(reverse("login"))


