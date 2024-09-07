from django.urls import path
from torii.contact.views import contact_form


app_name = 'contact'

urlpatterns = [
    path('contact/', contact_form,name="contact-form"),
]
