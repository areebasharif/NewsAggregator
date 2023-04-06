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
import speech_recognition as sr


# Create your views here.
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


def newscategory(request):

    articles = None

    # if request.GET:
    #     category = request.GET.get("category")
    #     url = f"https://newsapi.org/v2/top-headlines?language=en&category={category}&apiKey={API_KEY}"
    #     response = requests.get(url)
    #     data = response.json()
    #     articles = data["articles"]

    if request.POST:
        data = request.POST.dict()
        category = data["transcribed_text"]
        print("category ------------>", category)
        url = f"https://newsapi.org/v2/top-headlines?language=en&category={category}&apiKey={API_KEY}"
        response = requests.get(url)
        resp = response.json()
        articles = resp["articles"]

    context = {"articles": articles}

    return render(request, "newscategory2.html", context)

def bbc(request):
    newsapi = NewsApiClient(api_key="5e712cb029c5432e82fa92a5ec4083b2")
    topheadlines = newsapi.get_top_headlines(sources="cnn")
    articles = topheadlines["articles"]

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



def cnn(request):
    newsapi = NewsApiClient(api_key="5e712cb029c5432e82fa92a5ec4083b2")
    topheadlines = newsapi.get_top_headlines(sources="cnn")
    articles = topheadlines["articles"]

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


def espn(request):
    newsapi = NewsApiClient(api_key="5e712cb029c5432e82fa92a5ec4083b2")
    topheadlines = newsapi.get_top_headlines(sources="espn-cric-info")
    articles = topheadlines["articles"]

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


def login(request):
    return render(request, "login.html",)


def feedback(request):
    return render(request, "feedback.html",)


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
    messages.success(request, "Your message has been successfully sent")
    return render(request, "feedback.html")


def reg_form(request):
    if request.method == "POST":
        firstName = request.POST["firstName"]
    lastName = request.POST["lastName"]
    email = request.POST["email"]
    password = request.POST["password"]
    data = Registeration(
        firstName=firstName, lastName=lastName, email=email, password=password
    )

    data.save()
    return redirect("login")


# def transcribe_speech(audio_file):
#     r = sr.Recognizer()
#     with sr.AudioFile(audio_file) as source:
#         audio = r.record(source)
#     try:
#         # Transcribe the audio file into text
#         transcribed_text = r.recognize_google(audio)
#         return transcribed_text
#     except sr.UnknownValueError:
#         # Handle unrecognized speech
#         return ""


# def category_selection(request):

#     if request.method == "POST":
#         # Get the transcribed text from the user's spoken input
#         transcribed_text = transcribe_speech(audio_file)
#         response = requests.get(
#             f"https://newsapi.org/v2/top-headlines?category={transcribed_text}&apiKey=API_KEY"
#         )
#         articles = response.json().get("articles")

#         articles = []
#         for article_data in response.json().get("articles"):
#             article = {
#                 "title": article_data.get("title"),
#                 "description": article_data.get("description"),
#                 "url": article_data.get("url"),
#                 "image_url": article_data.get("urlToImage"),
#                 "published_at": article_data.get("publishedAt"),
#             }
#     articles.append(article)
#     # Render the filtered articles on a template
#     return render(request, "article_selection.html", {"articles": articles})

#     # Render the initial page with a form for voice input
#     return render(request, "voice.html")
