# Generated by Django 5.0.7 on 2024-09-17 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
