from django import forms
from torii.contact.models import Contact
from django_recaptcha.fields import ReCaptchaField

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'reason_for_contact', 'why_contact_us']
        labels = {
            'name': 'Nom',
            'email': 'E-mail',
            'phone_number': 'Numéro de téléphone',
            'reason_for_contact': 'Motif de contact',
            'why_contact_us': 'Donnez-nous plus de détails',
        }