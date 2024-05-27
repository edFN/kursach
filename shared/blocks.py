import logging

import pygments
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

logger = logging.getLogger(__name__)


class CardBlock(blocks.PageChooserBlock):
    pass


class TableCardBlock(blocks.StructBlock):
    count_column = blocks.IntegerBlock(label='Кол-во столбцов', min_value=1, max_value=5,
                                       required=True)
    count_row = blocks.IntegerBlock(label='Кол-во строк', min_value=1, max_value=5,
                                    required=True)
    pages = blocks.ListBlock(CardBlock(), min_num=1)

    def clean(self, value) -> dict:
        result = super().clean(value)

        if result['count_column'] * result['count_row'] < len(result['pages']):
            raise ValidationError('Количество страниц больше, чем отведенного места')

        return result


class TableImageBlock(blocks.StructBlock):
    count_column = blocks.IntegerBlock(label='Кол-во столбцов', min_value=1, max_value=5,
                                       required=True)
    count_row = blocks.IntegerBlock(label='Кол-во строк', min_value=1, max_value=5,
                                    required=True)
    images = blocks.ListBlock(ImageChooserBlock(label="Изображения"), min_num=1)

    def clean(self, value) -> dict:
        result = super().clean(value)

        if result['count_column'] * result['count_row'] < len(result['images']):
            raise ValidationError('Количество страниц больше, чем отведенного места')

        return result


class SliderPageBlock(blocks.StructBlock):
    type = blocks.ChoiceBlock(choices=(
        ("high", "high"),  # карточка занимает всю ширину
        ("small", "small")  # карточка занимает 33%
    ))
    pages = blocks.ListBlock(CardBlock(), min_num=1, max_num=5)


class SectionHeader(blocks.StructBlock):
    heading = blocks.RichTextBlock(features=['h2', 'h3', 'italic', 'bold', 'link'],
                                   verbose_name='Заголовок секции')


class SliderImageBlock(blocks.ListBlock):
    def __init__(self, *args, **kwargs):
        kwargs['child_block'] = ImageChooserBlock()
        super().__init__(*args, **kwargs)


class InformBlock(blocks.StructBlock):
    text = blocks.TextBlock(label="Текст", required=True)
    background = blocks.ChoiceBlock(label="Цвет фона", choices=(
        ("Зеленый", "Зеленый"),
        ("Красный", "Красный"),
        ("Желтый", "Желтый")
    ))

    class Meta:
        verbose_name = "Выделенный блок"
