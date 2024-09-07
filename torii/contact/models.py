from django.db import models
from django.core.validators import RegexValidator


phone_regex = RegexValidator(
    regex=r'^\+?\d{1,3}?\d{9,15}$',
    message="Le numéro de téléphone doit être au format '0555635254' ou '+indicatif555635254'.")

class Contact(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    why_contact_us = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f'{self.name} | {self.created_at}'