# Generated by Django 5.0.6 on 2024-06-01 10:16

import notification_app.models
import shared.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.snippets.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock()), ('slider_page', wagtail.blocks.StructBlock([('type', wagtail.blocks.ChoiceBlock(choices=[('high', 'high'), ('small', 'small')])), ('pages', wagtail.blocks.ListBlock(shared.blocks.CardBlock(), max_num=5, min_num=1))])), ('table_page', wagtail.blocks.StructBlock([('count_column', wagtail.blocks.IntegerBlock(label='Кол-во столбцов', max_value=5, min_value=1, required=True)), ('count_row', wagtail.blocks.IntegerBlock(label='Кол-во строк', max_value=5, min_value=1, required=True)), ('pages', wagtail.blocks.ListBlock(shared.blocks.CardBlock(), min_num=1))])), ('inform_block', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(label='Текст', required=True)), ('background', wagtail.blocks.ChoiceBlock(choices=[('Зеленый', 'Зеленый'), ('Красный', 'Красный'), ('Желтый', 'Желтый')], label='Цвет фона'))])), ('email_block', wagtail.snippets.blocks.SnippetChooserBlock(target_model=notification_app.models.SnippetRegisterForm))], blank=True, null=True, verbose_name='Содержимое'),
        ),
    ]
