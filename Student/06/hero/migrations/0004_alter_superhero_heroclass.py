# Generated by Django 4.2.4 on 2023-10-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_alter_superhero_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='heroClass',
            field=models.CharField(default='heroClass', max_length=200, null=True),
        ),
    ]
