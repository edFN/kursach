# Generated by Django 4.2.13 on 2024-06-03 14:27

from django.db import migrations
import shared.blocks
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0010_alter_articlereportmodel_report_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='content',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock()), ('slider_image', shared.blocks.SliderImageBlock()), ('inform_block', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(label='Текст', required=True)), ('background', wagtail.blocks.ChoiceBlock(choices=[('Зеленый', 'Зеленый'), ('Красный', 'Красный'), ('Желтый', 'Желтый')], label='Цвет фона'))])), ('table_image', wagtail.blocks.StructBlock([('count_column', wagtail.blocks.IntegerBlock(label='Кол-во столбцов', max_value=5, min_value=1, required=True)), ('count_row', wagtail.blocks.IntegerBlock(label='Кол-во строк', max_value=5, min_value=1, required=True)), ('images', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(label='Изображения'), min_num=1))])), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML'), ('c', 'C'), ('csharp', 'C#'), ('cpp', 'C++')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.blocks.TextBlock(identifier='code', label='Code'))])), ('document', wagtail.blocks.ListBlock(wagtail.documents.blocks.DocumentChooserBlock()))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articlereportmodel',
            name='report_items',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock()), ('slider_image', shared.blocks.SliderImageBlock()), ('inform_block', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(label='Текст', required=True)), ('background', wagtail.blocks.ChoiceBlock(choices=[('Зеленый', 'Зеленый'), ('Красный', 'Красный'), ('Желтый', 'Желтый')], label='Цвет фона'))])), ('table_image', wagtail.blocks.StructBlock([('count_column', wagtail.blocks.IntegerBlock(label='Кол-во столбцов', max_value=5, min_value=1, required=True)), ('count_row', wagtail.blocks.IntegerBlock(label='Кол-во строк', max_value=5, min_value=1, required=True)), ('images', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(label='Изображения'), min_num=1))])), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML'), ('c', 'C'), ('csharp', 'C#'), ('cpp', 'C++')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.blocks.TextBlock(identifier='code', label='Code'))])), ('document', wagtail.blocks.ListBlock(wagtail.documents.blocks.DocumentChooserBlock()))], blank=True, null=True),
        ),
    ]