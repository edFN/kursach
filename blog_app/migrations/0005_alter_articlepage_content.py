# Generated by Django 5.0.6 on 2024-05-26 17:08

import shared.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_alter_articlepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='content',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock()), ('slider_image', shared.blocks.SliderImageBlock()), ('inform_block', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(label='Текст', required=True)), ('background', wagtail.blocks.ChoiceBlock(choices=[('Зеленый', 'Зеленый'), ('Красный', 'Красный'), ('Желтый', 'Желтый')], label='Цвет фона'))])), ('table_image', wagtail.blocks.StructBlock([('count_column', wagtail.blocks.IntegerBlock(label='Кол-во столбцов', max_value=5, min_value=1, required=True)), ('count_row', wagtail.blocks.IntegerBlock(label='Кол-во строк', max_value=5, min_value=1, required=True)), ('images', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(label='Изображения'), min_num=1))]))], blank=True, null=True),
        ),
    ]
