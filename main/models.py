from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.CharField(max_length=255, verbose_name="Описание")


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')
    preview = models.ImageField(upload_to=None, height_field=None, width_field=None, verbose_name="Изображение")
    category = models.ForeignKey('main.Category', on_delete=models.CASCADE, verbose_name="Категория")
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateField(verbose_name="Дата создания")
    updated_at = models.DateField(verbose_name="Дата последнего изменения")
    manufactured_at = models.DateField(verbose_name="Дата производства")

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.Product = None
        self.Category = None

    def __str__(self):
        return f'{self.Category} {self.Product}'

    class Meta:
        verbose_name = 'продукты'
        verbose_name_plural = 'продукты'