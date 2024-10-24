
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base', views.BASE, name='base'),

    path('',views.HOME,name='home'),
    path('single/course',views.SINGLE_COURSE,name='single_course'),
    path('contact',views.CONTACT_US,name='contact_us'),
]
