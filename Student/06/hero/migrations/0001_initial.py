# Generated by Django 4.2.4 on 2023-09-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Hero Name', max_length=100)),
                ('identity', models.CharField(default='Civilian Name', max_length=100)),
                ('description', models.TextField(default='Description')),
                ('strength', models.CharField(default='Strength', max_length=100)),
                ('weakness', models.CharField(default='Weakness', max_length=100)),
                ('image', models.CharField(default='Image', max_length=100)),
            ],
        ),
    ]
