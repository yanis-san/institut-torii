from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.ForeignKey(to="SubjectType",on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to="img", blank=True, null=True)
    english_title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=100,blank=True)
    thumbnail = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self) -> str:
        return self.title



class Course(models.Model):
    ENROLLMENT_STATUS_CHOICES = [
        ('En cours', 'En cours'),
        ('Terminée', 'Terminée'),
    ]

    COURSE_TYPE_CHOICES = [
        ('individual', 'Individuel'),
        ('online', 'En ligne'),
        ('presential', 'Présentiel en groupe'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    frequency = models.CharField(max_length=100, blank=True, null=True)
    days = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    hour = models.TimeField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=COURSE_TYPE_CHOICES)
    duration=models.CharField(max_length=150,blank=True)
    price = models.IntegerField()
    subject = models.ForeignKey(to='Subject', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    thumbnail = models.URLField(max_length=200, blank=True, null=True)
    enrollment = models.CharField(
        max_length=10,
        choices=ENROLLMENT_STATUS_CHOICES,
        default='En cours',
    )

    def __str__(self):
        return f'{self.title} | {self.subject.title}'
    


class SubjectType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

    