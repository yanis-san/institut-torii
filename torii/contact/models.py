from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^(?:(?:\+213|0)(?:5|6|7)\d{8}|\+\d{1,3}\d{4,14})$',
    message="Le numéro de téléphone doit être au format algérien '0555324574' ou '+213555696868', ou international '+<indicatif><numéro>' (minimum 4 chiffres après l'indicatif, maximum 14 chiffres).")

class Contact(models.Model):
    JAPANESE_IN_PERSON = 'Cours de japonais en présentiel'
    JAPANESE_ONLINE = 'Cours de japonais en ligne'
    JAPANESE_INDIVIDUAL = 'Cours de japonais individuel'
    CHINESE_IN_PERSON = 'Cours de chinois en présentiel'
    CHINESE_ONLINE = 'Cours de chinois en ligne'
    CHINESE_INDIVIDUAL = 'Cours de chinois individuel'
    KOREAN_IN_PERSON = 'Cours de coréen en présentiel'
    KOREAN_ONLINE = 'Cours de coréen en ligne'
    KOREAN_INDIVIDUAL = 'Cours de coréen individuel'
    WORKSHOP = 'Atelier'
    OTHER = 'Autre'

    REASON_CHOICES = [
        (JAPANESE_IN_PERSON, 'Cours de japonais en présentiel'),
        (JAPANESE_ONLINE, 'Cours de japonais en ligne'),
        (JAPANESE_INDIVIDUAL, 'Cours de japonais individuel'),
        (CHINESE_IN_PERSON, 'Cours de chinois en présentiel'),
        (CHINESE_ONLINE, 'Cours de chinois en ligne'),
        (CHINESE_INDIVIDUAL, 'Cours de chinois individuel'),
        (KOREAN_IN_PERSON, 'Cours de coréen en présentiel'),
        (KOREAN_ONLINE, 'Cours de coréen en ligne'),
        (KOREAN_INDIVIDUAL, 'Cours de coréen individuel'),
        (WORKSHOP, 'Atelier'),
        (OTHER, 'Autre'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, validators=[phone_regex])
    reason_for_contact = models.CharField(max_length=50, choices=REASON_CHOICES, default=OTHER)
    why_contact_us = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} | {self.reason_for_contact} |{self.created_at}'
    
