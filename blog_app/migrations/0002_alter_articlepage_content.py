# Generated by Django 5.0.6 on 2024-05-26 10:43

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='content',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock()), ('slider_image', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))], blank=True, null=True),
        ),
    ]
