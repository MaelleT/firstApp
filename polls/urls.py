'''
Created on 30 mai 2016

@author: maelle
'''
from django.conf.urls import url

from . import views
urlpatterns=[
             url(r'$',views.index,name='index')
             ]