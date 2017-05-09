'''
Created on May 9, 2017

@author: Akhil Mathew
'''

from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ('id', 'name', 'is_company', 'image', 'mobile', 'email')