from django.shortcuts import render, redirect
from .scraper import *

# Create your views here.
def index(request):
    context = {
        "websites": websites
    }
    return render(request, "index.html", context)