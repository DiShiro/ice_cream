from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Contest(models.Model):
    title = models.CharField( 'Название', max_length=20)
    description = models.TextField('Описание')
    price = models.IntegerField(
        'Цена',
        help_text='Рекомендованная розничная цена',
        validators=[MinValueValidator(10), MaxValueValidator(100)],
    )
    comment = models.TextField('Комментарий', blank=True)