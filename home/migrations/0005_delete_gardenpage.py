# Generated by Django 3.1.2 on 2020-10-24 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('home', '0004_gardenpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GardenPage',
        ),
    ]
