# Generated by Django 3.0.8 on 2021-01-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20210123_1622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipeingredient',
            options={'verbose_name': 'ингредиент рецепта', 'verbose_name_plural': 'ингредиенты в рецепте'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='grocery_assistant/recipes/img/', verbose_name='Картинка'),
        ),
    ]