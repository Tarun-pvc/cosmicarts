from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import PostModel
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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


def create(request):
    posts = PostModel.objects.all()
    context = {"posts": posts}
    return render(request, template_name='login.html', context=context)


def details(request, pk):
    posts = PostModel.objects.filter(id=pk)
    context = {"posts": posts}
    return render(request, template_name='art_details.html', context=context)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        newuser = User.objects.create_user(
            username=username, email=email, password=password)
        newuser.save()

        messages.success(
            request, 'Congratulations! A New user has been saved.')

    return redirect('homepage')


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request=request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
        else:
            messages.error(request, 'Wrong Credentials!')
        return redirect('homepage')  # might need to change to ''
    # return render(request, template_name='home.html')


def openSignUp(request):
    return render(request=request, template_name='signup.html')


def openSignIn(request):
    return render(request, template_name='signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'Logged out!')
    return redirect('homepage')
