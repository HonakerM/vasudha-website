# Generated by Django 3.1.2 on 2020-10-24 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('garden', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_time', models.DateTimeField(auto_now_add=True)),
                ('fertilizer_time', models.DateTimeField(auto_now_add=True)),
                ('weed_time', models.DateTimeField(auto_now_add=True)),
                ('fertilizer_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fertilizer', to=settings.AUTH_USER_MODEL)),
                ('water_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='water', to=settings.AUTH_USER_MODEL)),
                ('weed_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='weed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
