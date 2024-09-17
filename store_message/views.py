
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StoreData
from django.contrib.auth.decorators import login_required

@csrf_exempt  # Use only if CSRF is not handled by the frontend
@login_required  # Ensure the user is logged in to submit the form
def contact_form(request):
    if request.method == 'POST':
        user = request.user  # Get the logged-in user
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save the form data in the StoreData model
        StoreData.objects.create(
            user=user,
            name=name,
            email=email,
            phone_number=phone,
            msg=message
        )

        return JsonResponse({'status': 'success', 'message': 'Form submitted successfully!'})
    
    return JsonResponse({'status': 'fail', 'message': 'Invalid request'}, status=400)


