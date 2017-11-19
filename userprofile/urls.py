from django.conf.urls import url , include
from django.contrib import admin
from . import views



app_name = 'userprofile'

urlpatterns = [
    url(r'^(?P<slug>[\w.@+-]+)/list$', views.Departmentwise_list ,name='Departmentwise_list'),
    url(r'^(?P<slug>[\w.@+-]+)/teaching$', views.Teaching_view ,name='profile_teaching'),
    url(r'^teaching/add$', views.Teaching_add ,name='profile_teaching_add'),
    url(r'^(?P<slug>[\w.@+-]+)/projecting$', views.Projecting_view ,name='profile_projecting'),
    url(r'^projecting/add$', views.Projecting_add ,name='profile_projecting_add'),
    url(r'^(?P<slug>[\w.@+-]+)/about_us$', views.About_us_view ,name='profile_about_us'),
    url(r'^profile_about_us$', views.About_us_create ,name='profile_about_us_create'),
    url(r'^(?P<slug>[\w.@+-]+)/about_us/edit$', views.About_us_edit ,name='profile_about_us_edit'),
    url(r'^StHome/', views.StHome, name="StHome"),
]
