"""
URL configuration for tourist_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
=======
from django.urls import path, include

urlpatterns = [
    path('', include('tourist_Info.urls')),
    path('admin/', admin.site.urls),
]
>>>>>>> 8da5056bc9c0ef8474439e7ec4c9b6cc57e3e5b9
