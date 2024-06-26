# Generated by Django 5.0.6 on 2024-05-26 12:37

import shared.blocks
import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_articlepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='content',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock()), ('slider_image', shared.blocks.SliderImageBlock()), ('inform_block', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(label='Текст', required=True)), ('background', wagtail.blocks.ChoiceBlock(choices=[('Зеленый', 'Зеленый'), ('Красный', 'Красный'), ('Желтый', 'Желтый')], label='Цвет фона'))]))], blank=True, null=True),
        ),
    ]
