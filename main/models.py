from django.db import models

# Create your models here.
from django.template.defaulttags import url

from main.utils import slugify


class News(models.Model):

    title = models.CharField(verbose_name='Название', max_length=100, default='Новая новость')
    slug = models.SlugField(verbose_name='slug (URL)', max_length=255, unique=True, db_index=True)
    teaser = models.TextField(verbose_name='Тизер', max_length=500, default='Тизер статьи')
    creation_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    author = models.CharField(verbose_name='Автор', max_length=100, default='Аноним')
    photo = models.FileField(verbose_name='Изображение статьи', upload_to='news_images/',
                             default='', blank=True)
    text = models.TextField(verbose_name='Текст статьи',
                            default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                                    'Ab commodi, consectetur dolores in iusto magni, nesciunt nulla '
                                    'possimus provident quis quos saepe? Animi cum distinctio dolore '
                                    'dolores et tempore, totam?')
    moderated = models.BooleanField(verbose_name="Опубликовать", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-update_date', '-creation_date', 'title']

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(force_insert, force_update, using, update_fields)
