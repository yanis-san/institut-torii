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

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    frequency = models.CharField(max_length=100)
    days = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    subject = models.ForeignKey(to='Subject',on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to="img", blank=True, null=True)


    def __str__(self):
        return f'{self.title} | {self.subject.title}'
    


class SubjectType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

    