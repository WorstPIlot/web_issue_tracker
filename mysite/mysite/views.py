from django.http import HttpResponse
from django.shortcuts import render
from .models import Issues


def index(request):
    issue = Issues.objects.all()
    return render(request, "index.html",
                  {'title': "Основная страница сайта", 'issue': issue
                   })
