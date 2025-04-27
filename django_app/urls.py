from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("members/", views.member_list, name="member_list"),
]
