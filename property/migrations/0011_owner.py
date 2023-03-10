# Generated by Django 2.2.24 on 2022-12-24 17:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20221223_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, verbose_name='ФИО владельца?')),
                ('phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца:')),
                ('normalized_phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца:')),
                ('ownership', models.ManyToManyField(blank=True, db_index=True, related_name='flats_owner', to='property.Flat', verbose_name='Квартиры в собственности:')),
            ],
        ),
    ]
