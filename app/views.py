from django.shortcuts import render
from .models import Item


def index(request):
    return render(request, "index.html")


def contacts_view(request):
    return render(request, "contacts.html")


def about_view(request):
    return render(request, "about.html")


def store_view(request):
    query = Item.objects.all()
    return render(request, "store.html", {"items": query})
