from django.shortcuts import render,redirect
from django.http  import HttpResponse 
from .models import Task

#14  create the addtask function and go to frontend to display the same
def addTask(request):
    
    task=request.POST['task']#15 this should be stored in the data base
    Task.objects.create(task=task)#15 Task is the model here , create is a built in function 
    return redirect('home')#15 after submitting the form it should redirect to the home page , should no go to AddTask url 