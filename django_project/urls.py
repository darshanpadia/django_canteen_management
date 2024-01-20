"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_view, name="home"),
    # path('signup/', signup_view, name="signup")


    path("accounts/", include("accounts.urls")),  #above our included Django auth app. Django will look top to bottom for URL patterns, so when it sees a URL route within our accounts app that matches one in the built-in auth app, it will choose the new accounts app route first.
    # path("accounts", include("django.contrib.auth.urls")), #To use the auth app. Django automatically installs the auth app when creating a new project. Look in the django_project/settings.py file under INSTALLED_APPS
    path("", TemplateView.as_view(template_name="home.html"), name="home"),  #To display the homepage. can also create dedicated pages app for this
    
]

