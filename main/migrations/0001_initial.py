# Generated by Django 5.0 on 2023-12-14 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecruiterInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('jobRole', models.CharField(blank=True, max_length=50, null=True)),
                ('dateOfJoining', models.DateField(blank=True, null=True)),
                ('packageOffered', models.CharField(max_length=50, null=True)),
                ('totalRounds', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentConsent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consent', models.BooleanField(default=False)),
                ('isHired', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SelectedStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roundQualifiedFor', models.IntegerField()),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.recruiterinfo')),
            ],
        ),
    ]
