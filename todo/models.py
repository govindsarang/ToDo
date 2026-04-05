from django.db import models
class Task(models.Model):
    task=models.CharField(max_length=250)
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)#for seeing when this data is created 
    updated_at=models.DateTimeField(auto_now=True)#for seeing when this data was updated or modified
    def __str__(self):#for string representation of model
        return self.task
    #8) after creating models.py we need to register the same model in the admin.py
      

