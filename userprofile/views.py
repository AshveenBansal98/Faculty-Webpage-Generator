from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import DetailView , ListView
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .forms import *
from .models import Teaching
from django.shortcuts import redirect, render_to_response
user = get_user_model()
# Create your views here.

def Departmentwise_list(request , slug):
    required_list = About_us.objects.filter(username__xyz__Department = slug)
    context={
        'Departmentwise_list':required_list,
        'Department':slug
    }
    return render(request, 'userprofile/Homepage.html', context)

def Teaching_view(request , slug):
    try:
        teaching = Teaching.objects.filter(username__username = slug)
        context={
            'teaching':teaching
        }
        return render(request, 'userprofile/teaching.html', context)
    except:
        return redirect('userprofile:profile_teaching_add')

# def Teaching_add(request):
#     if request.method == "POST":
#         form = teaching_add(request.POST)
#         if form.is_valid():
#             info = form.save(commit=False)
#             info.username = request.user
#             info.save()
#             return redirect('userprofile:profile_teaching', slug=request.user.username)
#     else:
#         form = teaching_add()
#         return render(request , 'userprofile/teaching_add.html' , {'form':form})

def Teaching_add(request):
    if(request.user.is_authenticated()):
        if request.method=="POST":
            Teaching.objects.all().delete()
            for i in range(int(request.POST.get("count"))):
                user = Teaching()
                user.username = request.user
                k=str(i+1)
                s="data"+k
                v=s+"2"
                # user.username=request.user.username
                user.Institute=str(request.POST.get(v))
                v=s+"3"
                user.Program=str(request.POST.get(v))
                v=s+"4"
                user.Branch=str(request.POST.get(v))
                v=s+"5"
                user.Duration=str(request.POST.get(v))
                user.save()
            return redirect('userprofile:profile_teaching_add')
        context = RequestContext(request)
        teaching = Teaching.objects.filter( username__username = request.user.username )
        context = {
            'teaching': teaching,
            #'Department': slug
        }
        return render(request, 'userprofile/teaching_add.html', context)
    else:
        return redirect("/accounts/login")

def Projecting_view(request , slug):
    try:
        projecting = Projecting.objects.filter(username__username = slug)
        context={
            'projecting':projecting
        }
        return render(request, 'userprofile/projecting.html', context)
    except:
        return redirect('userprofile:profile_projecting_add')

def Projecting_add(request):
    if request.method == "POST":
        form = projecting_add(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.username = request.user
            info.save()
            return redirect('userprofile:profile_projecting', slug=request.user.username)
    else:
        form = projecting_add()
        return render(request , 'userprofile/projecting_add.html' , {'form':form})

def About_us_view(request , slug ):
    try:
        about_us = About_us.objects.get(username__username = slug)
        user = get_user_model()
        context = {
           'about_us': about_us
        }
        return render(request, 'userprofile/detail_about_us.html', context)
    except:
        return redirect('userprofile:profile_about_us_create')

def About_us_create(request):
    if request.method == "POST":
        form = about_us_form(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.username = request.user
            info.save()
            return redirect('userprofile:profile_about_us', slug=request.user.username)
    else:
        form = about_us_form()
        return render(request , 'userprofile/about_us_edit.html' , {'form':form})

def About_us_edit(request , slug):
    about_us = About_us.objects.get(username__username = slug)
    if request.method == "POST":
        form = about_us_form(request.POST, instance=about_us)
        if form.is_valid():
            form.save()
            return redirect('userprofile:profile_about_us', slug)
    else:
        form = about_us_form(instance=about_us)
        return render(request , 'userprofile/about_us_edit.html' , {'form':form})


def StHome(request):
    if(request.user.is_authenticated()):
        context = RequestContext(request)
        awards = Awards.objects.filter( username__username = request.user.username)
        teaching = Teaching.objects.filter( username__username = request.user.username)
        education = Education.objects.filter( username__username = request.user.username)
        experience = Experience.objects.filter( username__username = request.user.username)
        projecting = Projecting.objects.filter( username__username = request.user.username)
        publications = Publications.objects.filter( username__username = request.user.username)
        about_us = About_us.objects.filter( username__username = request.user.username)
        context = {
          'awards': awards,
          'teaching': teaching,
          'about_us': about_us,
          'education': education,
          'experience': experience,
          'projecting': projecting,
          'publications': publications,
        }
        return render(request, 'userprofile/StHome.html', context)
    else:
        return redirect("/accounts/login")
