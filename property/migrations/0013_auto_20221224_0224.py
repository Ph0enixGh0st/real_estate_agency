# Generated by Django 2.2.24 on 2022-12-23 23:24

from django.db import migrations
from property.models import Flat, Complaint, Owner

def link_flats(apps, schema_editor):

    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        object, created = Owner.objects.update_or_create(
            owner=flat.owner,
            owner_phonenumber=flat.owners_phonenumber,
            owner_normalized_phonenumber=flat.pure_phonenumber,
            )
        if not created:
            object.ownership.set([flat])

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20221224_0054'),
    ]

    operations = [
        migrations.RunPython(link_flats)
    ]