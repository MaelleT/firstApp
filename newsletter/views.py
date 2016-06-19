from django.shortcuts import render
from django.http import request

from .forms import ContactForm, SignUpForm
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from firstApp import settings
# Create yoursviews here.
def home(request):
    title = "welcome"
    if request.user.is_authenticated():
        title = "Welcome %s" %(request.user.username)
  
    #===========================================================================
    # print(request)
    # if request.method =="POST":
    #     print(request.POST)
    #===========================================================================
    form = SignUpForm(request.POST or None)
    
    context = {
        "title" : title,
        "form" : form
            }
    
    if form.is_valid():
        print(request.POST['email'])#not recommended
        instance=form.save(commit=False)
        #or form.save()
        #=======================================================================
        # if not instance.full_name :
        #     instance.full_name = 'georges' 
        # 
        #=======================================================================
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name=full_name
        instance.save()
        #print(instance)
        #print(instance.timestamp)
        
        context = {
            "title" : "Thank you",
                  }
    return render(request,"bases.html",context)


def contact(request):
    form = ContactForm(request.POST or None)
    context ={'form':form}
    if form.is_valid():
        for key in form.cleaned_data :
            print (key)
            print (form.cleaned_data.get(key))
        subject ='Test django email'
        message = form.cleaned_data.get('message')
        to_email = [form.cleaned_data.get('email'),settings.EMAIL_HOST_USER]
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject,
                  message,
                  from_email ,to_email,fail_silently=False) 
        #=======================================================================
        # email = form.cleaned_data.get('email')
        # message = form.cleaned_data.get('message')
        # full_name=form.cleaned_data.get('full_name')
        # print(email,message,full_name) # façon d'afficher le contenu des variables du formulaire
        #=======================================================================
    return render(request,"forms.html",context)




