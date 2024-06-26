# Generated by Django 4.2.13 on 2024-05-29 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0093_uploadedfile'),
        ('blog_app', '0007_alter_articlepage_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleListPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.categoryarticle', verbose_name='Категории статей')),
            ],
            options={
                'verbose_name': 'Список статей',
            },
            bases=('wagtailcore.page',),
        ),
    ]
