from django.contrib import admin

from main import models


# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug', 'is_published', 'created', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'stock', 'is_published', 'created', 'updated')
    list_filter = ('created', 'updated', 'is_published', 'category')
    list_editable = ('price', 'stock', 'is_published')
    search_fields = ('name', 'description')