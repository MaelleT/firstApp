from django.contrib import admin

# Register your models here.
from .models import SignUp


class SignUpAdmin(admin.ModelAdmin):
    #permet de personnaliser l'interface admin
    list_display = ["__str__","timestamp"]
    class Meta :
        model = SignUp
    

admin.site.register(SignUp,SignUpAdmin)
