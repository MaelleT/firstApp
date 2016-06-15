from django.shortcuts import render
from django.http import request

from .forms import SignUpForm
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
    return render(request,"home.html",context)

