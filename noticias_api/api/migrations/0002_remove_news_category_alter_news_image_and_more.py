# Generated by Django 4.2.7 on 2023-12-17 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category_id',
            field=models.IntegerField(default=1),
        ),
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='news/'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
