from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def user_create(request):
    if request.method == 'POST':
        return HttpResponse('')
    else:
        return HttpResponse('', status=500)
