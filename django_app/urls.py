from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("members/", views.member_list, name="member_list"),
    path(
        "member_list_template/", views.member_list_template, name="member_list_template"
    ),
    path(
        "member_list_template/details/<uuid:member_id>",
        views.member_details,
        name="member_details",
    ),
]
