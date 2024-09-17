
from django.urls import path
from .views import contact_form


urlpatterns = [
    path('submit-form/', contact_form, name='submit_form'),
]
