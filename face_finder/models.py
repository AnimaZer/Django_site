from django.db import models

# Create your models here.
class FaceFinder(models.Model):
  title = models.TextField('Введите имя', max_length=30)
  imageIn = models.ImageField('Выберите изображение', upload_to='images/')
  videoIn = models.FileField('Выберите видео файл', upload_to='videos/')
  def __str__(self):
    return self.title
