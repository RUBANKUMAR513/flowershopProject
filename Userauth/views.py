from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token

@csrf_exempt
def custom_login_view(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

# this file is very important