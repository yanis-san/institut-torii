# Generated by Django 5.1.1 on 2024-09-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0013_course_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
