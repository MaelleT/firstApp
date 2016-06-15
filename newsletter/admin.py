from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SignUpForm


class SignUpAdmin(admin.ModelAdmin):
    #permet de personnaliser l'interface admin
    list_display = ["__str__","timestamp"]
    form = SignUpForm
    
    #before create forms : SignUpForm
    #class Meta :
    #    model = SignUp
    

admin.site.register(SignUp,SignUpAdmin)
