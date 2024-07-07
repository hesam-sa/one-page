from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def http_test(request):
    return HttpResponse('This is an HTTP response')

def json_test(request):
    return JsonResponse({'name':'ali'})