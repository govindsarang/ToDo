from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse 
from .models import Task

#14  create the addtask function and go to frontend to display the same
def addTask(request): 
    task=request.POST['task']#15 this should be stored in the data base
    Task.objects.create(task=task)#15 Task is the model here , create is a built in function 
    return redirect('home')#15 after submitting the form it should redirect to the home page , should no go to AddTask url 
#for 16 go to views.py i todo_main
def mark_as_done(request,pk):
    task=get_object_or_404(Task,pk=pk)#fetch the data from the data base or 404 error
    task.is_completed = True
    task.save()
    return redirect('home') 
def mark_as_undone(request,pk):
    task=get_object_or_404(Task,pk=pk)#fetch the data from the data base or 404 error
    task.is_completed = False
    task.save()
    return redirect('home') 
def edit_task(request,pk):
    get_task=get_object_or_404(Task,pk=pk)
    if request.method =='POST':
        new_task=request .POST['task']
        get_task.task =new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task' :get_task,   
        }
        return render(request, 'edit_task.html',context)
def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')
  
