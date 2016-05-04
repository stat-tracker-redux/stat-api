from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.


@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        return HttpResponse('')
    else:
        return HttpResponse('', status=500)
