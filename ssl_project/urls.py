"""ssl_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^accounts/', include('accounts.urls')),
    url(r"^$", views.Homepage, name="home"),
    url(r"^thanks/$", views.Thankspage, name="thanks"),
    url(r"^test/", views.TestPage.as_view(), name="test"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^profile/" , include('userprofile.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard', views.dashboard, name="dashboard"),
    url(r'^profile/about_us_create/', views.About_us_create, name="profile_about_us_create"),
    url(r'^profile/about_us_edit/', views.About_us_edit, name="profile_about_us_edit"),
    url(r'^experience/', views.experience, name="experience"),
    url(r'^teaching/', views.teaching, name="teaching"),
    url(r'^education/', views.education, name="education"),
    url(r'^template/', views.template, name="template"),
    url(r'^resume/', views.resume, name="resume"),
    url(r'^publications/', views.publications, name="publications"),
    url(r'^StHome/', views.StHome, name="StHome"),
    url(r'^Font/', views.Font, name="Font"),
]
