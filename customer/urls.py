'''
Created on May 9, 2017

@author: Akhil Mathew
'''

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from customer import views

urlpatterns = [
    
    url(r'^(?P<pk>[0-9]+)$', views.CustomerDetail.as_view()),
    url(r'^', views.CustomerList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)