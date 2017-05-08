'''
Created on May 8, 2017

@author: Akhil Mathew
'''

from django.conf.urls import url,include
from snippets.views import snippet_detail,snippet_list


urlpatterns = [
    
    url(r'^snippets/$', snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail),    
    
]
