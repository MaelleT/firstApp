'''
Created on 12 juin 2016

@author: maelle
'''
from django.conf.urls import url
from newsletter import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'newsletter'
urlpatterns=[
            url(r'^home/$',views.home,name='home'),
            url(r'^contact/$',views.contact,name='contact'),

                 ]
             
if (settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    