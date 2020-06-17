"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from facebook.views import play
from facebook.views import play2
from facebook.views import my_profile
from facebook.views import event
from facebook.views import myFail
from facebook.views import myHelp
from facebook.views import myWarn
from facebook.views import newsFeed
from facebook.views import detail_feed
from facebook.views import pages
from facebook.views import new_feed
from facebook.views import edit_feed, remove_feed
from facebook.views import new_page, edit_page, remove_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('play/', play),
    path('play2/', play2),
    path('shin/profile/', my_profile),
    path('event/', event),
    path('fail/', myFail),
    path('help/', myHelp),
    path('warn/', myWarn),
    path('', newsFeed),
    path('feed/<pk>/', detail_feed),
    path('feed/<pk>/remove', remove_feed),
    path('feed/<pk>/edit', edit_feed),
    path('new/', new_feed),
    path('pages/', pages),
    path('pages/new/', new_page),
    path('pages/edit/<pk>/', edit_page),
    path('pages/remove/<pk>/', remove_page),
]
