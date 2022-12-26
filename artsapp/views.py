from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import PostModel
# a list view is a *LIST* of all the objects
# Detail View is something like the data about one Object


def homepage(request):
    posts = PostModel.objects.all()
    context = {"posts": posts}
    return render(request, template_name='home.html', context=context)


def about(request):
    return render(request, template_name='about.html')


def contact(request):
    return render(request, template_name='contact.html')


def portfolio(request):
    return render(request, template_name='portfolio.html')


def login(request):
    return render(request, template_name='login.html')


def create(request):
    posts = PostModel.objects.all()
    context = {"posts": posts}
    return render(request, template_name='login.html', context=context)


def details(request, pk):
    posts = PostModel.objects.filter(id=pk)
    context = {"posts": posts}
    return render(request, template_name='art_details.html', context=context)
