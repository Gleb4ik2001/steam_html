from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
import random


def index(request:HttpRequest)->HttpResponse:
    return render(
        request=request,
        template_name='games/index.html',
        context={}
    )

def about(request:HttpRequest)->HttpResponse:
    return render(
        template_name='games/about.html',
        request=request,
        context={}
    )