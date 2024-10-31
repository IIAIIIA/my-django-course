from email.policy import default

from django.db import models
from django.urls import reverse


# Create your models here.
# MVC   = MTV в Django
# Model = Model
# View  = Template
# Controller = View

# При работе с шаблонами мы используем 3 основных момента
#   1)Директивы = переменные {{  }}
#   2)Теги = блоки (циклы, условия) {%  %}
#   3)Фильтры, применяются в основном к переменным     |

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название новости')
    content = models.TextField(blank=True, verbose_name='Содержание новости')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=False, verbose_name='Статус публикации')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование категории', db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['title']
