# Generated by Django 2.2.7 on 2019-11-15 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191115_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktailingredientunit',
            name='cocktail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='app.Cocktail'),
        ),
    ]