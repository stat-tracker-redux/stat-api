import json
from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


# Create your views here.


@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        # user = User.objects.create_user('superlunk360', 'todd.mcbuffy@gmail.com', 'supersecret')

        body = request.body.decode('utf-8')
        user_info = json.loads(body)
        try:
            user = User.objects.create_user(user_info['username'],
                                            user_info['email'],
                                            user_info['password'])
            user.save()
        except KeyError:
            return HttpResponse('Please use the correct JSON format', status=400)

        return HttpResponse('')  # TODO: add message
    else:
        return HttpResponse('', status=500)  # TODO: add message


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def logout(request):
    Token.objects.get(user=request.user).delete()
    return HttpResponse('')
