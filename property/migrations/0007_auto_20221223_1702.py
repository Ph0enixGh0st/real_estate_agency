# Generated by Django 2.2.24 on 2022-12-23 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to='property.Flat', verbose_name='Кол-во лайков'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complaint',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Текст жалобы:'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='yelps', to='property.Flat', verbose_name='Квартира, на которую пожаловались:'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='yelps', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался:'),
        ),
    ]
