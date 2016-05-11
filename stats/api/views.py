import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.


@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        # user = User.objects.create_user('superlunk360', 'todd.mcbuffy@gmail.com', 'supersecret')

        body = request.body.decode('utf-8')
        # user_info = json.loads(body)
        # user = User.objects.create_user(user_info['username'],
        #                                 user_info['email'],
        #                                 user_info['password'])
        #
        # user.save()

        return HttpResponse('')
    else:
        return HttpResponse('', status=500)
