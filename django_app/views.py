from django.http import HttpResponse
from rest_framework import status
from django.shortcuts import render
from django.template import loader
from .models import Member
from django.http import JsonResponse


def home(request):
    template = loader.get_template("django_template.html")
    return HttpResponse(template.render())


def member_list(request):
    members = Member.objects.all()
    data = []
    for member in members:
        data.append(
            {
                "member_id": str(member.member_id),
                "firstname": member.firstname,
                "lastname": member.lastname,
            }
        )
    return JsonResponse(data, safe=False)


def member_list_template(request):
    members = Member.objects.all().values()
    return render(request, "all_members.html", {"members": members})


def member_details(request, member_id):
    members = Member.objects.get(member_id=member_id)
    return render(request, "member_details.html", {"members": members})
