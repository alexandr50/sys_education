from django.db import models



class Product(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец', related_name='owner')
    name = models.CharField(max_length=50, verbose_name='Название')
    students = models.ManyToManyField('users.User', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class UserProduct(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Владелец')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name='Продукт')

    class Meta:
        verbose_name = 'Продукт пользователя'
        verbose_name_plural = 'Продукты пользователя'
