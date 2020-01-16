from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
import json

def login(request):
    if (request.method == 'POST'):
        body = json.loads(request.body)
        try:
            user = User.objects.get(email=body['login'])
        except User.DoesNotExist:
            return JsonResponse({
                'message': 'Login ou senha errada.'
            }, status=400)
        else:
            if user.check_password(body['senha']):
                refresh = RefreshToken.for_user(user)
                return JsonResponse({
                    'token': str(refresh.access_token),
                    'refresh': str(refresh),
                })
            return JsonResponse({
                'message': 'Login ou senha errada.'
            }, status=400)

def signup(request):
    if (request.method == 'POST'):
        body = json.loads(request.body)
        user = User.objects.create_user(body['email'], body['email'], body['password'])
        user.save()
            
