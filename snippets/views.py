from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippets
from snippets.serializers import SnippetSerializer
# Create your views here.


@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
        
        
#view corresponds to individual snippets

@csrf_exempt
def snippet_detail(request, pk):
    
    try:
        snippet = get_object_or_404(Snippets, pk=pk)
    except Snippets.DoesNotExist:
        return HttpResponse(404)
    else:
        if request.method == 'GET':
            serializer = SnippetSerializer(snippet)
            return JsonResponse(serializer.data)
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = SnippetSerializer(snippet, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors, status=400)
        elif request.method == 'DELETE':
            snippet.delete()
            return HttpResponse(status=204)
    
    
    
    
            
        
