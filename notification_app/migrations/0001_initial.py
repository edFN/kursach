# Generated by Django 4.2.13 on 2024-05-29 13:40

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationEmailRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email пользователя')),
            ],
            options={
                'verbose_name': 'Электронная почта',
                'verbose_name_plural': 'Электронная почта для рассылки',
            },
        ),
        migrations.CreateModel(
            name='SnippetRegisterForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Название')),
                ('text', wagtail.fields.RichTextField(blank=True, verbose_name='Текст')),
                ('text_success', wagtail.fields.RichTextField(blank=True, verbose_name='Текст успешной регистрации Email')),
            ],
            options={
                'verbose_name': 'Блок приема Email пользователя',
            },
        ),
    ]