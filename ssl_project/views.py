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
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import re


class TestPage(TemplateView):
    template_name = "test.html"

class ThanksPage(TemplateView):
    template_name = "index.html"

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


def Homepage(request):
    required_list = About_us.objects.all()
    context={
        'list':required_list,
    }
    return render(request, 'index.html', context)

def Thankspage(request):
    required_list = About_us.objects.all()
    context={
        'list':required_list,
    }
    return render(request, 'thanks.html', context)

def experience(request):
    if(request.user.is_authenticated()):
        if request.method=="POST":
            Experience.objects.filter(username__username = request.user.username).delete()
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
            Awards.objects.filter(username__username = request.user.username).delete()
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
            Publications.objects.filter(username__username = request.user.username).delete()
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
            Projecting.objects.filter(username__username = request.user.username).delete()
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
            Education.objects.filter(username__username = request.user.username).delete()
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
            about_us = About_us.objects.filter(username__username = request.user.username)
            if about_us[0].sync=="No":
                context = {
                   'about_us': About_us.objects.get(username__username = request.user.username)
                }
                return render(request, 'dashboard.html', context)
            # Education.objects.filter(username__username = request.user.username).delete()
            # Experience.objects.filter(username__username = request.user.username).delete()
            # Awards.objects.filter(username__username = request.user.username).delete()
            experience = Experience.objects.filter(username__username = request.user.username)
            Publications.objects.filter(username__username = request.user.username).delete()
            awards = Awards.objects.filter(username__username = request.user.username)
            education = Education.objects.filter(username__username = request.user.username)
            ed1 = len(education)
            ex1 = len(experience)
            a1 = len(awards)
            html = urlopen("file://" + str(about_us[0].path))
            soup = BeautifulSoup(html, "lxml")
            #python3 Education.py /home/ashveen/Downloads/file4.html > Education.csv
            colleges = []
            degree = []
            branch = []
            times = []
            for tags in soup.findAll('section', attrs = {'class': 'pv-profile-section education-section ember-view'} ):
                for h3 in  tags.findAll('h3', attrs = {'class': 'Sans-17px-black-85%-semibold'} ):
                    colleges.append(h3.text)
                count = 0
                for span in  tags.findAll('span', attrs = {'class': 'pv-entity__comma-item'} ):
                    count = count + 1
                    if count%2 == 1:
                        degree.append(span.text)
                    else:
                        branch.append(span.text)
                for p in  tags.findAll('p', attrs = {'class': 'pv-entity__dates Sans-15px-black-70%'} ):
                    count1 = 0
                    for span in p.findAll('span'):
                        count1 = count1 + 1
                        if count1 == 2:
                            x=0
                            for time in span.findAll('time'):
                                x = x+1
                                if (x == 1):
                                    t = time.text
                                if (x == 2):
                                    times.append(t + " - " + time.text)
                                    break

            for i in range(0, len(times)):
                p1=0
                for j in range(0, ed1):
                    if(colleges[i] == education[j].Institute and degree[i] == education[j].Program and branch[i] == education[j].Branch and times[i] == education[j].Duration ):
                        p1=1
                        break
                if p1==0 :
                    user=Education()
                    user.username = request.user
                    user.Institute=colleges[i]
                    user.Program=degree[i]
                    user.Branch=branch[i]
                    user.Duration=times[i]
                    user.save()

            # python3 Education.py /home/ashveen/Downloads/file4.html > Experience.csv
            designations = []
            companies = []
            dates = []

            for tags in soup.findAll('section', attrs = {'class': 'pv-profile-section experience-section ember-view'} ):
                for h3 in  tags.findAll('h3', attrs = {'class': 'Sans-17px-black-85%-semibold'} ):
                    designations.append(h3.text)
                for span in  tags.findAll('span', attrs = {'class': 'pv-entity__secondary-title'} ):
                    companies.append(span.text)
                for h4 in  tags.findAll('h4', attrs = {'class': 'pv-entity__date-range inline-block Sans-15px-black-70%'} ):
                    count = 0
                    for span in h4.findAll('span'):
                        count = count + 1
                        if count == 2:
                            dates.append(span.text)



            for i in range(0, len(designations)):
                p1=0
                for j in range(0, ex1):
                    if(designations[i] == experience[j].Designation and companies[i] == experience[j].Company and dates[i] == experience[j].Duration):
                        p1=1
                        break
                if p1==0:
                    user=Experience()
                    user.username = request.user
                    user.Designation=designations[i]
                    user.Company=companies[i]
                    user.Duration=dates[i]
                    user.save()
                    #print(designations[i] + "|" + companies[i] + "|" + dates[i])

            title = []
            date = []
            issuer = []
            desc = []

            for div in soup.findAll('div', attrs = {'class': 'pv-accomplishments-block__list-container'} ):
                for h4 in div.findAll('h4', attrs = {'class': 'pv-accomplishment-entity__title'} ):
                    t = h4.text
                    t = t.replace('honor title', '')
                    t = t.replace('\n  ', '')
                    t = t.replace('\n', '')
                    title.append(t)

            for p in soup.findAll('p', attrs = {'class': 'pv-accomplishment-entity__subtitle'} ):
                for span in p.findAll('span', attrs = {'class': 'pv-accomplishment-entity__date'} ):
                    t = span.text
                    t = t.replace('\nhonor date\n', '')
                    t = t.replace('\n', '')
                    t = t.replace('  ', '')
                    date.append(t)
                for span in p.findAll('span', attrs = {'class': 'pv-accomplishment-entity__issuer'} ):
                    t = span.text
                    t = t.replace('\nhonor issuer\n', '')
                    t = t.replace('\n', '')
                    t = t.replace('  ', '')
                    issuer.append(t)


            for p in soup.findAll('p', attrs = {'class': 'pv-accomplishment-entity__description Sans-15px-black-70%'} ):
                t = p.text
                t = t.replace('\nhonor description\n', '')
                t = t.replace('\n', '')
                t = t.replace('  ', '')
                desc.append(t)

            for i in range(0, len(title)):
                p1=0
                for j in range(0, a1):
                    if(title[i] == awards[j].Title and date[i] == awards[j].Date and issuer[i] == awards[j].Issuer):
                        p1=1
                        break
                if p1==0:
                    user=Awards()
                    user.username = request.user
                    user.Title=title[i]
                    user.Date=date[i]
                    user.Issuer=issuer[i]
                    if i<len(desc):
                        user.Description=desc[i]
                    else:
                        user.Description=""
                    user.save()

            ur = str(about_us[0].scholar)
            html1 = urlopen(ur)
            soup1 = BeautifulSoup(html1, "lxml")
            article = []
            year = []
            authors = []
            citations = []
            for table in soup1.findAll('table', attrs = {'id': 'gsc_a_t'} ):
                for row in table.findAll('tr', attrs = {'class': 'gsc_a_tr'} ):
                    for a in  row.findAll('a', attrs = {'class': 'gsc_a_at'} ):
                        article.append(a.text)
                        count = 0
                    for div in  row.findAll('div', attrs = {'class': 'gs_gray'} ):
                        count = count + 1
                        if count == 1:
                            authors.append(div.text)
                    for tags in row.findAll('td', attrs = {'class': 'gsc_a_c'} ):
                        for a in  tags.findAll('a', attrs = {'class': 'gsc_a_ac gs_ibl'} ):
                            citations.append(a.text)
                    for tags in row.findAll('td', attrs = {'class': 'gsc_a_y'} ):
                        for a in  tags.findAll('span', attrs = {'class': 'gsc_a_h gsc_a_hc gs_ibl'} ):
                            year.append(a.text)

            for i in range(0, len(article)):
                user=Publications()
                user.username = request.user
                user.Title=article[i]
                user.URL=ur
                user.Year=year[i]
                user.Citations=citations[i]
                user.Abstract=authors[i]
                user.save()

            context = {
               'about_us': About_us.objects.get(username__username = request.user.username)
            }
            # url = ""
            # for div in soup.findAll('div', attrs = {'class': ' presence-entity__image EntityPhoto-circle-8 ember-view'} ):
            #     url = div.attrs

            # url2 = str(url)
            # link = re.findall(r'"([^"]*)"', url2)
            # about = About_us.objects.filter( username__username = request.user.username )
            # if len(about)!=0:
            #     about2 = About_us()
            #     about2.username = about[0].username
            #     about2.Name = about[0].Name
            #     about2.Department = about[0].Department
            #     about2.Institute = about[0].Institute
            #     about2.Departmental_post = about[0].Departmental_post
            #     about2.Room_no = about[0].Room_no
            #     about2.Phone = about[0].Phone
            #     about2.Email = about[0].Email
            #     about2.Address = about[0].Address
            #     about2.ResearchInterest = about[0].ResearchInterest
            #     about2.LinkedinURL = about[0].LinkedinURL
            #     about2.path = about[0].path
            #     about2.scholar = about[0].scholar
            #     if len(link)!=0:
            #         about2.img=link[0]
            #     else:
            #         about2.img="https://upload.wikimedia.org/wikipedia/en/thumb/1/12/IIT_Guwahati_Logo.svg/1014px-IIT_Guwahati_Logo.svg.png"
            #     About_us.objects.filter(username__username = request.user.username).delete()
            #     about2.save()

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
                a=info.path
                html = urlopen("file://" + str(a))
                soup = BeautifulSoup(html, "lxml")
                url = ""
                for div in soup.findAll('div', attrs = {'class': ' presence-entity__image EntityPhoto-circle-8 ember-view'} ):
                    url = div.attrs
                url2 = str(url)
                link = re.findall(r'"([^"]*)"', url2)
                info.Image=link[0]
                info.save()
                #python3 Education.py /home/ashveen/Downloads/file4.html > Education.csv
                colleges = []
                degree = []
                branch = []
                times = []
                for tags in soup.findAll('section', attrs = {'class': 'pv-profile-section education-section ember-view'} ):
                    for h3 in  tags.findAll('h3', attrs = {'class': 'Sans-17px-black-85%-semibold'} ):
                        colleges.append(h3.text)
                    count = 0
                    for span in  tags.findAll('span', attrs = {'class': 'pv-entity__comma-item'} ):
                        count = count + 1
                        if count%2 == 1:
                            degree.append(span.text)
                        else:
                            branch.append(span.text)
                    for p in  tags.findAll('p', attrs = {'class': 'pv-entity__dates Sans-15px-black-70%'} ):
                        count1 = 0
                        for span in p.findAll('span'):
                            count1 = count1 + 1
                            if count1 == 2:
                                x=0
                                for time in span.findAll('time'):
                                    x = x+1
                                    if (x == 1):
                                        t = time.text
                                    if (x == 2):
                                        times.append(t + " - " + time.text)
                                        break

                for i in range(0, len(times)):
                    user = Education()
                    user.username = request.user
                    user.Institute=colleges[i]
                    user.Program=degree[i]
                    user.Branch=branch[i]
                    user.Duration=times[i]
                    user.save()

                # python3 Education.py /home/ashveen/Downloads/file4.html > Experience.csv
                designations = []
                companies = []
                dates = []

                for tags in soup.findAll('section', attrs = {'class': 'pv-profile-section experience-section ember-view'} ):
                    for h3 in  tags.findAll('h3', attrs = {'class': 'Sans-17px-black-85%-semibold'} ):
                        designations.append(h3.text)
                    for span in  tags.findAll('span', attrs = {'class': 'pv-entity__secondary-title'} ):
                        companies.append(span.text)
                    for h4 in  tags.findAll('h4', attrs = {'class': 'pv-entity__date-range inline-block Sans-15px-black-70%'} ):
                        count = 0
                        for span in h4.findAll('span'):
                            count = count + 1
                            if count == 2:
                                dates.append(span.text)



                for i in range(0, len(designations)):
                    user=Experience()
                    user.username = request.user
                    user.Designation=designations[i]
                    user.Company=companies[i]
                    user.Duration=dates[i]
                    user.save()
                    #print(designations[i] + "|" + companies[i] + "|" + dates[i])

                title = []
                date = []
                issuer = []
                desc = []

                for div in soup.findAll('div', attrs = {'class': 'pv-accomplishments-block__list-container'} ):
                    for h4 in div.findAll('h4', attrs = {'class': 'pv-accomplishment-entity__title'} ):
                        t = h4.text
                        t = t.replace('honor title', '')
                        t = t.replace('\n  ', '')
                        t = t.replace('\n', '')
                        title.append(t)

                for p in soup.findAll('p', attrs = {'class': 'pv-accomplishment-entity__subtitle'} ):
                    for span in p.findAll('span', attrs = {'class': 'pv-accomplishment-entity__date'} ):
                        t = span.text
                        t = t.replace('\nhonor date\n', '')
                        t = t.replace('\n', '')
                        t = t.replace('  ', '')
                        date.append(t)
                    for span in p.findAll('span', attrs = {'class': 'pv-accomplishment-entity__issuer'} ):
                        t = span.text
                        t = t.replace('\nhonor issuer\n', '')
                        t = t.replace('\n', '')
                        t = t.replace('  ', '')
                        issuer.append(t)


                for p in soup.findAll('p', attrs = {'class': 'pv-accomplishment-entity__description Sans-15px-black-70%'} ):
                    t = p.text
                    t = t.replace('\nhonor description\n', '')
                    t = t.replace('\n', '')
                    t = t.replace('  ', '')
                    desc.append(t)

                for i in range(0, len(title)):
                    user=Awards()
                    user.username = request.user
                    user.Title=title[i]
                    user.Date=date[i]
                    user.Issuer=issuer[i]
                    if i<len(desc):
                        user.Description=desc[i]
                    else:
                        user.Description=""
                    user.save()

                ur = str(info.scholar)
                html1 = urlopen(str(ur))
                soup1 = BeautifulSoup(html1, "lxml")
                article = []
                year = []
                authors = []
                citations = []
                for table in soup1.findAll('table', attrs = {'id': 'gsc_a_t'} ):
                    for row in table.findAll('tr', attrs = {'class': 'gsc_a_tr'} ):
                        for a in  row.findAll('a', attrs = {'class': 'gsc_a_at'} ):
                            article.append(a.text)
                            count = 0
                        for div in  row.findAll('div', attrs = {'class': 'gs_gray'} ):
                            count = count + 1
                            if count == 1:
                                authors.append(div.text)
                        for tags in row.findAll('td', attrs = {'class': 'gsc_a_c'} ):
                            for a in  tags.findAll('a', attrs = {'class': 'gsc_a_ac gs_ibl'} ):
                                citations.append(a.text)
                        for tags in row.findAll('td', attrs = {'class': 'gsc_a_y'} ):
                            for a in  tags.findAll('span', attrs = {'class': 'gsc_a_h gsc_a_hc gs_ibl'} ):
                                year.append(a.text)

                for i in range(0, len(article)):
                    user=Publications()
                    user.username = request.user
                    user.Title=article[i]
                    user.URL=ur
                    user.Year=year[i]
                    user.Citations=citations[i]
                    user.Abstract=authors[i]
                    user.save()

                # url = ""
                # for div in soup.findAll('div', attrs = {'class': ' presence-entity__image EntityPhoto-circle-8 ember-view'} ):
                #     url = div.attrs

                # url2 = str(url)
                # link = re.findall(r'"([^"]*)"', url2)
                # about = About_us.objects.filter( username__username = request.user.username )
                # if len(about)!=0:
                #     about2 = About_us()
                #     about2.username = about[0].username
                #     about2.Name = about[0].Name
                #     about2.Department = about[0].Department
                #     about2.Institute = about[0].Institute
                #     about2.Departmental_post = about[0].Departmental_post
                #     about2.Room_no = about[0].Room_no
                #     about2.Phone = about[0].Phone
                #     about2.Email = about[0].Email
                #     about2.Address = about[0].Address
                #     about2.ResearchInterest = about[0].ResearchInterest
                #     about2.LinkedinURL = about[0].LinkedinURL
                #     about2.path = about[0].path
                #     if len(link)!=0:
                #         about2.img=link[0]
                #     else:
                #         about2.img="https://upload.wikimedia.org/wikipedia/en/thumb/1/12/IIT_Guwahati_Logo.svg/1014px-IIT_Guwahati_Logo.svg.png"
                #     about2.save()

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
