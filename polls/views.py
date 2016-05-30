#from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
from .models import Question
# for each view : all django wants is that HttpResponse. Or an exception.

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    
    #use template
    template = loader.get_template('polls/index.html')
    context={
             'latest_question_list':latest_question_list
             }
    
    #sans le template
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    
    return HttpResponse(template.render(context,request))

def detail(request,question_id):
    return HttpResponse("You are looking at question %s" % question_id)

def results(request,question_id):
    return HttpResponse("You are looking at the results of question %s" % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s" % question_id)