'''
Created on May 8, 2017

@author: Akhil Mathew
'''

from rest_framework import serializers
from models import Snippets

class SnippetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Snippets
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
