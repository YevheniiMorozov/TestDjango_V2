# Generated by Django 4.0.3 on 2022-03-28 15:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='approve_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(default=2, max_length=150),
            preserve_default=False,
        ),
    ]
