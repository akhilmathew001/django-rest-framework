'''
Created on May 7, 2017

@author: Akhil Mathew
'''

from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        fields = ('url', 'username', 'email', 'groups')
        

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        fields = ('url', 'name')        