from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.CharField(max_length=255, verbose_name="Описание")

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')
    preview = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(max_length=5, verbose_name="Цена")
    dateOfCreation = models.DateField(verbose_name="Дата создания")
    dateOfLastEdit = models.DateField(verbose_name="Дата последнего изменения")

    def __str__(self):
        return f'{self.Category} {self.Product}'

    class Meta:
        verbose_name = 'продукты'
        verbose_name_plural = 'продукты'