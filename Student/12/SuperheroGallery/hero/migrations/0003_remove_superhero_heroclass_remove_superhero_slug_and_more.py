# Generated by Django 4.2.4 on 2023-11-14 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hero.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hero', '0002_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superhero',
            name='heroClass',
        ),
        migrations.RemoveField(
            model_name='superhero',
            name='slug',
        ),
        migrations.AlterField(
            model_name='superhero',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='identity',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=hero.models.get_upload),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='strength',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='weakness',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.CreateModel(
            name='Investigator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name', max_length=100)),
                ('user', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='investigator',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='hero.investigator'),
        ),
        migrations.AddField(
            model_name='superhero',
            name='investigator',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='hero.investigator'),
        ),
    ]
