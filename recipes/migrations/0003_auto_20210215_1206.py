# Generated by Django 3.0.8 on 2021-02-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20210214_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(choices=[('breakfast', 'breakfast'), ('Обед', 'lunch'), ('Ужин', 'dinner')], db_index=True, max_length=50, verbose_name='Имя тега'),
        ),
    ]