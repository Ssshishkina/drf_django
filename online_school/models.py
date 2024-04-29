from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    image = models.ImageField(upload_to='courses_image', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='lessons_image', verbose_name='Превью', **NULLABLE)
    video_link = models.URLField(verbose_name='Ссылка', help_text='Укажите ссылку на видео', **NULLABLE)
    course = models.ForeignKey(Course, related_name='courses', on_delete=models.CASCADE,
                               verbose_name='Курс')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
