# Generated by Django 5.0.7 on 2024-09-17 11:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.DateTimeField(auto_now_add=True)),
                ('accept', models.BooleanField(default=False)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsciption_to', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsciption_from', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
