from django.db import models



class Product(models.Model):
    owner = models.ForeignKey('User', on_delete=models.SET_NULL, verbose_name='владелец')
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
