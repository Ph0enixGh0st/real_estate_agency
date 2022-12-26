# Generated by Django 2.2.24 on 2022-12-23 18:42

from django.db import migrations
import phonenumbers

def populate_normalized_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    
    flats = Flat.objects.all()
    for flat in flats.iterator():
        if flat.owners_phonenumber:
            unparsed_number = flat.owners_phonenumber
            parsed_number = phonenumbers.parse(unparsed_number, 'RU')
            if phonenumbers.is_possible_number(parsed_number) and phonenumbers.is_valid_number(parsed_number):
                flat.pure_phonenumber = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
                flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_flat_pure_phonenumber'),
    ]

    operations = [
        migrations.RunPython(populate_normalized_numbers)
    ]
