'''
Created on 30 mai 2016

@author: maelle
'''
from django.conf.urls import url

from . import views

# define namespaces for project with a lot of apps : URL

app_name = 'polls'
urlpatterns=[
            url(r'^$',views.IndexView.as_view(),name='index'),
             #ex /polls/5
            url(r'^(?P<question_id>[0-9]+)/$',views.TheDetailView.as_view(),name='detail'),
            #url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'), #sans vue generic
            #ex /polls/5/results/
            url(r'^(?P<question_id>[0-9]+)/results/$',views.ResultsView.as_view(),name='results'),
             #ex /polls/5/vote
            url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote')

             ]