# Generated by Django 5.0.1 on 2024-01-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drawing', '0003_alter_drawingtables_drawing'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawingtables',
            name='details',
            field=models.TextField(default='test', verbose_name='Інформація'),
        ),
        migrations.AddField(
            model_name='drawingtables',
            name='picture',
            field=models.ImageField(default='drw_p/test.jpg', upload_to='drw_p'),
        ),
    ]
