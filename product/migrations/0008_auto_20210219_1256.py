# Generated by Django 3.1.6 on 2021-02-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_merge_20210219_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='goal',
            name='icon',
            field=models.URLField(default=2, max_length=2000),
            preserve_default=False,
        ),
    ]
