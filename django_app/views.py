from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status


def home(request):
    return HttpResponse(status.HTTP_200_OK)


# Create your views here.
