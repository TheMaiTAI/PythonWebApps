# Generated by Django 4.2.4 on 2023-09-29 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='heroClass',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='superhero',
            name='slug',
            field=models.SlugField(default='hero-name', unique=True),
        ),
    ]
