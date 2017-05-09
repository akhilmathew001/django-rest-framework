'''
Created on May 8, 2017

@author: Akhil Mathew
'''

from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import snippet_detail,snippet_list


urlpatterns = [
    
    url(r'^snippets/$', snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail),    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
