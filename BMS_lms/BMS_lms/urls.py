
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .import views, user_login

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base', views.BASE, name='base'),

    path('',views.HOME,name='home'),
    path('courses',views.SINGLE_COURSE,name='single_course'),
    path('courses/filter-data',views.filter_data,name='filter-data'),
    path('contact',views.CONTACT_US,name='contact_us'),
    path('about',views.ABOUT_US,name='about_us'),
    path('search',views.SEARCH_COURSE,name="search_course"),

    path('accounts/register',user_login.REGISTER,name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('do_Login',user_login.DO_LOGIN, name='doLogin'),
    path('accounts/profile',user_login.PROFILE,name='profile'),
    path('account/profile/update',user_login.PROFILE_UPDATE, name='profile_update'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
