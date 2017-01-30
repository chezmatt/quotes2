from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
import bcrypt

# Create your views here.
def index(request):

    return render(request, "quotes/index.html")


def registration(request):
    pass

def login(request):
    pass

def logout(request):
    pass

def postreview(request):
    pass
# this is here!
