
from rest_framework.views import APIView
from customer.models import Customer
from customer.serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.

class CustomerList(APIView):
    
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = CustomerSerializer(request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CustomerDetail(APIView):
    
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self, pk): 
        try:
            customer = Customer.objects.get(pk=pk)
            return customer
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)   
    
    
    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
            
            