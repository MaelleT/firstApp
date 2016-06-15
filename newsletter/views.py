from django.shortcuts import render
from django.http import request

# Create yoursviews here.
def home(request):
    title = "welcome"
    if request.user.is_authenticated():
        title = "Welcome %s" %(request.user.username)
    
    #add a form
    context = {
                   "title" : title,
                  } 
    return render(request,"home.html",context)

