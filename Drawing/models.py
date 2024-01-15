from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


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
    picture = models.ImageField(upload_to='drw_p', default='drw_p/test.jpg')
    details = models.TextField(verbose_name="Інформація", default='test')
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Час")


    def __str__(self):
        return f'Кресленя'

    class Meta:
        verbose_name = "Кресленя"
        verbose_name_plural = "Кресленя"

# Create your models here.
