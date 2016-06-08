from django.db import models
from datetime import timezone, date, datetime

# Create your models here.
# Each model is represented by a class that subclasses django.db.models.Mode
# Each model has a number of class variables, each of which represents a database field in the model.
# Each field is represented by an instance of a Field class 
# The name of each Field instance (e.g. question_text or pub_date) is the field’s name, in machine-friendly format. You’ll use this value in your Python code, and your database will use it as the column name.
# You can use an optional first positional argument to a Field to designate a human-readable name
import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published(self):
        #before unittest 
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()
    
       
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
    