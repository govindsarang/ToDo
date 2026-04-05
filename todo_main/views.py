from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
def home(request):#2 so in urls page we created a path called home which will direct to views.py and this function always accepts the rquests
    tasks=Task.objects.filter(is_completed=False).order_by('-updated_at')#9-filter  #16 orderby which sorts the task in ascending order depentding on what time u updated the task
    completed_tasks=Task.objects.filter(is_completed=True)#17 to view all the things that are completed
    context={
        'tasks':tasks, #9 for viewing the tasks in the frontend , for the next step go to home .html line 38
        'completed_tasks':completed_tasks,  #18 this gives all the completed tasks under completed_task, for viewing this got to home.html compltered tasks
    }
    return render(request,'home.html',context)#context should be present in the home page so adding context to home page
    #return HttpResponse('<h1>Home Page</h1>')#http response created so import this http response
#3 is creating bootstrap before creating logic in the backend , create frontend
#for creating frontend create a new folder called as templates in todo main folder
#then inside the templates folder first create html file