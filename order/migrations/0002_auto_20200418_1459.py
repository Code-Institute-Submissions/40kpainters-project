# Generated by Django 3.0.5 on 2020-04-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_form',
            name='comments',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='order_form',
            name='scheme',
            field=models.TextField(max_length=500),
        ),
    ]