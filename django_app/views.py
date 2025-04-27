from django.http import HttpResponse
from rest_framework import status
from django.template import loader


def home(request):
    template = loader.get_template("django_template.html")
    return HttpResponse(template.render({}, request))


# Create your views here.
