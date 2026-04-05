"""
URL configuration for todo_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from . import views#1 importing views for home but views is not there in todo main folder so create a views file


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name='home'),#1 creating home page  ,#2 in the views page
    #ToDo 
    path('todo/',include('todo.urls')),#12 creating todo path but before that create urls.py in todo app folder then next step is there in urls.py of to do app
]
