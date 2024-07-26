# Generated by Django 3.2.4 on 2024-07-26 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letra_1', models.CharField(max_length=1)),
                ('tiempo_1', models.FloatField(default=0.0)),
                ('letra_2', models.CharField(max_length=1)),
                ('tiempo_2', models.FloatField(default=0.0)),
                ('letra_3', models.CharField(max_length=1)),
                ('tiempo_3', models.FloatField(default=0.0)),
                ('letra_4', models.CharField(max_length=1)),
                ('tiempo_4', models.FloatField(default=0.0)),
                ('letra_5', models.CharField(max_length=1)),
                ('tiempo_5', models.FloatField(default=0.0)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
