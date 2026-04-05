from django.urls import path  #13 
from . import views
#13 create a url of path which say add task and name is addtask so it will go to add task  go to line 79 in home.html
#now go to views.py and set up 
urlpatterns=[
    path('addTask/',views.addTask,name='addTask'),
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),#18 adding url pattern for marks as done
    path('mark_as_undone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),
    #edit feature
    path('edit_task/<int:pk>/' ,views.edit_task, name='edit_task'),
    path('delete_task/<int:pk>/',views.delete_task, name='delete_task'), 
]