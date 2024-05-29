from django.shortcuts import render
# For the authentication, login, and password we should import
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
# If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user) 
           return HttpResponseRedirect(reverse("index"))
        else: 
            return render(request, "users/login.html", {
                "message": "invalid credentials"
            })
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return render(request, "user/login.html", {
        "message": "Logged out"
    })

