# Generated by Django 5.1.7 on 2025-05-24 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('japan_foods', '0006_alter_food_ingredients_alter_food_recepie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=30, null=True, verbose_name='שם הכותב')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='japan_foods.author', verbose_name='הכותב'),
        ),
    ]
