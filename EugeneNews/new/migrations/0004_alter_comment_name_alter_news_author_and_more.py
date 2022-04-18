# Generated by Django 4.0.3 on 2022-03-31 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('new', '0003_alter_comment_name_alter_news_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='RegisterUser',
        ),
    ]
