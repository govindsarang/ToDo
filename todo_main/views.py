from django.http import HttpResponse
from django.shortcuts import render
def home(request):#2 so in urls page we created a path called home which will direct to views.py and this function always accepts the rquests
    return render(request,'home.html')
    #return HttpResponse('<h1>Home Page</h1>')#http response created so import this http response
#3 is creating bootstrap before creating logic in the backend , create frontend
#for creating frontend create a new folder called as templates in todo main folder
#then inside the templates folder first create html file