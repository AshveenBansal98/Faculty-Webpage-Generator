from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import DetailView , ListView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from userprofile.models import *
from userprofile.forms import *
import csv

class TestPage(TemplateView):
    template_name = "test.html"

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            if request.user.is_authenticated():
                context={
                    'user':request.user
                }
                return render(request , "index.html" , context)
        return super().get(request, *args, **kwargs)


def experience(request):
    if(request.user.is_authenticated()):
        if request.method=="POST":
            Experience.objects.all().delete()
            for i in range(int(request.POST.get("count"))):
                user = Experience()
                user.username = request.user
                k=str(i+1)
                s="data"+k
                v=s+"2"
                # user.username=request.user.username
                user.Designation=str(request.POST.get(v))
                v=s+"3"
                user.Company=str(request.POST.get(v))
                v=s+"4"
                user.Duration=str(request.POST.get(v))
                user.save()
            Awards.objects.all().delete()
            for i in range(int(request.POST.get("counta"))):
                user = Awards()
                user.username = request.user
                k=str(i+1)
                s="award"+k
                v=s+"2"
                # user.username=request.user.username
                user.Title=str(request.POST.get(v))
                v=s+"3"
                user.Date=str(request.POST.get(v))
                v=s+"4"
                user.Issuer=str(request.POST.get(v))
                v=s+"5"
                user.Description=str(request.POST.get(v))
                user.save()
            return redirect('experience')
        context = RequestContext(request)
        experience = Experience.objects.filter( username__username = request.user.username )
        awards = Awards.objects.filter( username__username = request.user.username )
        context = {
            'experience': experience,
            'awards': awards,
            #'Department': slug
        }
        return render(request, 'experience.html', context)
    else:
        return redirect("/accounts/login")

def publications(request):
    if(request.user.is_authenticated()):
        if request.method=="POST":
            Publications.objects.all().delete()
            for i in range(int(request.POST.get("count"))):
                user = Publications()
                user.username = request.user
                k=str(i+1)
                s="data"+k
                v=s+"2"
                # user.username=request.user.username
                user.Title=str(request.POST.get(v))
                v=s+"3"
                user.URL=str(request.POST.get(v))
                v=s+"4"
                user.Year=str(request.POST.get(v))
                v=s+"5"
                user.Citations=str(request.POST.get(v))
                v=s+"6"
                user.Abstract=str(request.POST.get(v))
                user.save()
            Projecting.objects.all().delete()
            for i in range(int(request.POST.get("countp"))):
                user = Projecting()
                user.username = request.user
                k=str(i+1)
                s="project"+k
                v=s+"2"
                # user.username=request.user.username
                user.Topic=str(request.POST.get(v))
                v=s+"3"
                user.Details=str(request.POST.get(v))
                v=s+"4"
                user.Year=str(request.POST.get(v))
                user.save()
            return redirect('publications')
        context = RequestContext(request)
        publications = Publications.objects.filter( username__username = request.user.username )
        projecting = Projecting.objects.filter( username__username = request.user.username )
        context = {
            'publications': publications,
            'projecting': projecting,
            #'Department': slug
        }
        return render(request, 'publications.html', context)
    else:
        return redirect("/accounts/login")

def education(request):
    if(request.user.is_authenticated()):
        if request.method=="POST":
            Education.objects.all().delete()
            for i in range(int(request.POST.get("count"))):
                user = Education()
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
            return redirect('education')
        context = RequestContext(request)
        education = Education.objects.filter( username__username = request.user.username )
        context = {
            'education': education,
            #'Department': slug
        }
        return render(request, 'education.html', context)
    else:
        return redirect("/accounts/login")

# def dashboard(request):
#     if(request.user.is_authenticated()):
#         return render(request, 'dashboard.html')
#     else:
#         return redirect("/accounts/login")

def dashboard(request):
    if(request.user.is_authenticated()):
        try:
            about_us = About_us.objects.get(username__username = request.user.username)
            user = get_user_model()
            context = {
               'about_us': about_us
            }
            return render(request, 'dashboard.html', context)
        except:
            return redirect('profile_about_us_create')
    else:
        return redirect("/accounts/login")

def About_us_create(request):
    if(request.user.is_authenticated()):
        if request.method == "POST":
            form = about_us_form(request.POST)
            if form.is_valid():
                info = form.save(commit=False)
                info.username = request.user
                info.save()
                return redirect('dashboard')
            else:
                form = about_us_form(instance=about_us)
                return render(request , 'about_us_edit.html' , {'form':form})
        else:
            form = about_us_form()
            return render(request , 'about_us_edit.html' , {'form':form})
    else:
        return redirect("/accounts/login")

def About_us_edit(request):
    if(request.user.is_authenticated()):
        about_us = About_us.objects.get(username__username = request.user.username)
        if request.method == "POST":
            form = about_us_form(request.POST, instance=about_us)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
            else:
                form = about_us_form(instance=about_us)
                return render(request , 'about_us_edit.html' , {'form':form})
    else:
        return redirect("/accounts/login")

def StHome(request):
    if(request.user.is_authenticated()):
        return render(request, 'StHome.html')
    else:
        return redirect("/accounts/login")

def Font(request):
    if(request.user.is_authenticated()):
        return render(request, 'Font.html')
    else:
        return redirect("/accounts/login")

# def publications(request):
#     if(request.user.is_authenticated()):
#         return render(request, 'publications.html')
#     else:
#         return redirect("/accounts/login")

def resume(request):
    if(request.user.is_authenticated()):
        return render(request, 'resume.html')
    else:
        return redirect("/accounts/login")

# def education(request):
#     if(request.user.is_authenticated()):
#         return render(request, 'education.html')
#     else:
#         return redirect("/accounts/login")

def template(request):
    if(request.user.is_authenticated()):
        return render(request, 'template.html')
    else:
        return redirect("/accounts/login")

def teaching(request):
    if(request.user.is_authenticated()):
        return render(request, 'teaching.html')
    else:
        return redirect("/accounts/login")

# def experience(request):
#     if(request.user.is_authenticated()):
#         return render(request, 'experience.html')
#     else:
#         return redirect("/accounts/login")
#         return redirect("/accounts/login")
