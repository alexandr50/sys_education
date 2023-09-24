from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    product = models.ManyToManyField('products.Product', blank=True, verbose_name='Продукт')
    link = models.URLField(verbose_name='Ссылка')
    duration = models.DurationField(verbose_name='Продолжительнось')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продолжительность'
        verbose_name_plural = 'Продолжительности'
