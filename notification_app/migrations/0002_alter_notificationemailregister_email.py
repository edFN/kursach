# Generated by Django 4.2.13 on 2024-05-30 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationemailregister',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='Email пользователя'),
        ),
    ]