# Generated by Django 2.2.7 on 2019-11-15 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cocktailingredientunit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='(no title)', max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cocktail',
            name='recipe',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='cocktailingredientunit',
            name='unit',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Unit'),
        ),
        migrations.AddField(
            model_name='cocktailingredientunit',
            name='ingredient',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Ingredient'),
        ),
    ]