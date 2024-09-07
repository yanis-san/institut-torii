from django import forms
from torii.contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', "why_contact_us"]
        labels = {"name": "Nom", "email":"E-mail", "phone_number":"Numéro de téléphone", "why_contact_us":"Motif de contact"}
