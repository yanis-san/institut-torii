# Generated by Django 5.1.1 on 2024-09-14 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0012_alter_course_frequency'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.CharField(choices=[('individual', 'Individuel'), ('online', 'En ligne'), ('presential', 'Présentiel en groupe')], default='', max_length=20),
            preserve_default=False,
        ),
    ]