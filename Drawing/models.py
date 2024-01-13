from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    avatar = models.ImageField(upload_to='avatar', default='avatar/avatar_crj2ayQ.jpg')
    status = models.CharField(max_length=1, verbose_name="Статус")
    info = models.TextField(verbose_name="Інформація")

    def __str__(self):
        return f'Додаткова інформація'

    class Meta:
        verbose_name = "Користувач додаток"
        verbose_name_plural = "Користувачі додаток"

class DrawingTables(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    drawing = models.FileField(upload_to='drw', default='drw/test.pdf')

    def __str__(self):
        return f'Кресленя'

    class Meta:
        verbose_name = "Кресленя"
        verbose_name_plural = "Кресленя"

# Create your models here.
