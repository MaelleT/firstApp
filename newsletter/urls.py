'''
Created on 12 juin 2016

@author: maelle
'''
from django.conf.urls import url
from newsletter import views

app_name = 'newsletter'
urlpatterns=[
            url(r'^home/$',views.home,name='home'),
            url(r'^contact/$',views.contact,name='contact'),

             ]