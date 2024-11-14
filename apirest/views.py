from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings
from urllib.parse import urlencode
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def callback(request):
    code = request.GET.get('code')

    if not code:
        return JsonResponse({'error': 'No authorization code found'}, status=400)

    print('entrando')
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': 'my-django-app',  # El client_id de tu cliente en Keycloak
        'client_secret': 'aPJargZqekYevHZ9rDKgX7o4ETwHu34X',  # Si tienes un client_secret configurado en Keycloak
    }

    token_url = 'http://localhost:8080/realms/Mercadito/protocol/openid-connect/token'

    response = requests.post(token_url, data=data)

    print(response, 'response')

    if response.status_code != 200:
        return JsonResponse({'error': 'Invalid authorization code'}, status=400)

    tokens = response.json()

    access_token = tokens['access_token']
    id_token = tokens['id_token']

    return JsonResponse({'access_token': access_token, 'id_token': id_token})