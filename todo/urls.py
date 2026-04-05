from django.urls import path  #13 
from . import views
#13 create a url of path which say add task and name is addtask so it will go to add task  go to line 79 in home.html
#now go to views.py and set up 
urlpatterns=[
    path('addTask/',views.addTask,name='addTask'),
]