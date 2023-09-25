from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    product = models.ManyToManyField('products.Product', blank=True, verbose_name='Продукт')
    link = models.URLField(verbose_name='Ссылка')
    duration = models.DurationField(default=None, verbose_name='Продолжительнось')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class UserLesson(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Владелец')
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE, verbose_name='Урок')
    watched_time = models.DurationField(verbose_name='Просмотренно времени')
    last_watched = models.DateTimeField(auto_now=True, verbose_name='Дата последенго просмотра')

    @property
    def status(self):
        if (self.watched_time / self.lesson.duration) > 0.8:
            return 'Просмотренно'
        return 'Не просмотренно'

    def __str__(self):
        return f'{self.owner} | {self.lesson}'

    class Meta:
        verbose_name = 'Урок пользователя'
        verbose_name_plural = 'Урок пользователя'
