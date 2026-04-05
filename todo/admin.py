from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):#11for checking at backend whether the particular task in completed or not 
    list_display=('task','is_completed','updated_at')#11 these are the field from the models.py that we have created
    search_fields=('task',)#11 for adding the search in backend , next step is add task which is presen in frontend should be functional so for that go to url.py
admin.site.register(Task,TaskAdmin)
 #after registrations we need to make migrations and migrate the files
 #so in terminal we need to write makemigrations
 #after making migrations new migration file is created as 0001_initial.py
 #then apply the migrated file to the database
 #so for this run the commane manage.py migrate where all the tables wil be created
 #next logic is we need to ass task from frontend so for this we have to got to views
#for the next step go to the views.py where the logic is present  