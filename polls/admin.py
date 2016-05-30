from django.contrib import admin
from .models import Question,Choice

# Register your models here.
admin.site.register(Question) # permet d'administrer le model Question depuis l'interface admin
admin.site.register(Choice)