from django.db import models


# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(blank=True,null=True,max_length=120)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    
    def __str__(self):  # __str__
        return self.email
        