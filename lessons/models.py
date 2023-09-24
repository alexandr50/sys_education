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

class UserLesson(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Владелец')
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE, verbose_name='Урок')
    watched_time = models.DurationField(verbose_name='Просмотренно времени')

    class Meta:
        verbose_name = 'Урок пользователя'
        verbose_name_plural = 'Урок пользователя'
