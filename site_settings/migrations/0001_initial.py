# Generated by Django 5.0.6 on 2024-05-22 11:30

import autoslug.fields
import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=True, populate_from=models.CharField(max_length=100))),
                ('link_url', models.CharField(max_length=500)),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_title', models.CharField(blank=True, max_length=50, null=True)),
                ('link_url', models.CharField(max_length=500)),
                ('open_in_new_tab', models.BooleanField(default=False)),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.page')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_menu', to='site_settings.menu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True, verbose_name='Название сайта')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон для связи')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта для связи')),
                ('owner_info', models.CharField(blank=True, max_length=80, null=True, verbose_name='ФИО владельца сайта')),
                ('footer_menu', models.ManyToManyField(blank=True, null=True, related_name='footer_menu_rel', to='site_settings.menu', verbose_name='Меню в подваде')),
                ('page_terms_condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.page', verbose_name='Страница политики и конфенденциальности')),
            ],
            options={
                'verbose_name': 'Основные настройки сайта',
                'verbose_name_plural': 'Основные настройки сайта',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaSettingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('type', models.CharField(choices=[('ВК', 'ВК'), ('Youtube', 'Youtube'), ('Телеграм', 'Телеграм'), ('Одноклассники', 'Одноклассники')], max_length=80, verbose_name='Платформа')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка на страницу')),
                ('setting', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_site_settings_rel', to='site_settings.sitesettings')),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
    ]
