# Generated by Django 4.1.2 on 2022-10-30 16:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^(\\+?\\d{0,4})?\\s?-?\\s?(\\(?\\d{3}\\)?)\\s?-?\\s?(\\(?\\d{3}\\)?)\\s?-?\\s?(\\(?\\d{4}\\)?)?$', 'The phone number provided is invalid')])),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=255, null=True)),
                ('status', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=True)),
                ('type', models.BooleanField(default=False)),
            ],
        ),
    ]
