'''
Created on 30 mai 2016

@author: maelle
'''
from django.conf.urls import url

from . import views
from django.conf.urls import include
from django.contrib.auth.views import login

# define namespaces for project with a lot of apps : URL

app_name = 'polls'
# explication des URL
#'r' pour 'raw' impose l'interprétation de toute la chaine de caractères 
# '$' end-of-string match character
# paramètres entre parenthèses seront capturés de l'URL : toujours de type string
# 
# Named regular-expression (?P<name>pattern) : name is the name of the group and pattern is some pattern to match
# extra-otion should be passed in a URL 
# url(r'^blog/(?P<year>[0-9]{4})/$', views.year_archive, {'foo': 'bar'})
# /blog/2005/, Django will call views.year_archive(request, year='2005', foo='bar').

# in the URL template tag, the parameter name should be used for reverse resolution

# the as_view method créé une instance de la classe et appelle la méthode dispatch 
# des attributs de classe peuvent être transmis en paramètre de la fonction

# Decorating class-based views
# url(r'^about/', login_required(TemplateView.as_view(template_name="secret.html")))
# url(r'^vote/', permission_required('polls.can_vote')(VoteView.as_view()))


urlpatterns=[
            url(r'^$',views.IndexView.as_view(),name='index'),
            
            #ex /polls/5
            # call the function views.index(request,question_id='5')
            url(r'^(?P<question_id>[0-9]+)/$',views.TheDetailView.as_view(),name='detail'),
            #url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'), #sans vue generic
            
            #ex /polls/5/results/
            # call the function views.results(request,question_id='5')
            url(r'^(?P<question_id>[0-9]+)/results/$',views.ResultsView.as_view(),name='results'),
            
            
            #ex /polls/5/vote
            url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
            
            #for authentication
            url(r'^login/$', 'django.contrib.auth.views.login'),
            url(r'^logout/$', 'django.contrib.auth.views.logout')
            
             ]