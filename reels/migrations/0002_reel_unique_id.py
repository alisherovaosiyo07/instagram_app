# Generated by Django 5.0.7 on 2024-10-21 12:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reel',
            name='unique_id',
            field=models.CharField(blank=True, help_text="Bu yerda faqat 12ta lik random string, number va symboldan iborat bo'ladi va siz buni yaratishiz shart emas, dastur o'zi yaratib beradi", max_length=90, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='hato_boldi', message='Bu symbollardan tashqari ?&^', regex='^(?=.*[A-Za-z])(?=.*\\d)(?=.*[@$!%*])[^?&^]{-}$')]),
        ),
    ]
