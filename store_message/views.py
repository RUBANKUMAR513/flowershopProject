
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only use this if CSRF tokens aren't managed in the frontend
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name,email,phone,message)
        # Save data or process it further as needed
        # Example: Contact.objects.create(name=name, email=email, phone=phone, message=message)

        return JsonResponse({'status': 'success', 'message': 'Form submitted successfully!'})
    return JsonResponse({'status': 'fail', 'message': 'Invalid request'}, status=400)
