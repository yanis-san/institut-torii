# Generated by Django 5.1.1 on 2024-09-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0005_subject_english_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
