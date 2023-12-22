# Generated by Django 5.0 on 2023-12-18 09:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentconsent',
            name='consent',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studentconsent',
            name='isHired',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studentconsent',
            name='recruiter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentConsent', to='main.recruiterinfo'),
        ),
        migrations.AlterField(
            model_name='studentconsent',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentConsent', to=settings.AUTH_USER_MODEL),
        ),
    ]