# Generated by Django 4.2.8 on 2023-12-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_locais'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
    ]
