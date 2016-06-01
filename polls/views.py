#from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.template import loader
from .models import Question

from django.shortcuts import render, get_object_or_404
# for each view : all django wants is that HttpResponse. Or an exception.
from .models import Choice,Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    
    context={'latest_question_list':latest_question_list}
    
    return render(request,'polls/index.html',context)
  
    #use template without shortcut
    #template = loader.get_template('polls/index.html')
    #context={'latest_question_list':latest_question_list}
    #return HttpResponse(template.render(context,request))

    #sans le template
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    


def detail(request,question_id):
    try :
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    #le bloc try except peut être remplacé par get_object_or_404(Question,pk=question_id)
    
    return render(request,'polls/detail.html',{'question':question})


def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request,'polls/results.html',{'question':question})
    #return HttpResponse("You are looking at the results of question %s" % question_id)

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)

    try :
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist): #KeyError may be raised by request.POST if key does not exist
        #redisplaying the question voting
        return render(request,'polls/detail.html',{'question' : question, 'error_message':"You didn't select a choice"})
    else :
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
        
    # before coding the behaviour
    #return HttpResponse("You are voting on question %s" % question_id)



