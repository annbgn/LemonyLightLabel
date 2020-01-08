from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contacts/", views.contacts_view, name="contacts_view"),
    path("about/", views.about_view, name="about_view"),
    path("store/", views.store_view, name="store_view"),
]
