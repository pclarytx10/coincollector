# Generated by Django 4.1.5 on 2023-02-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_coin_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='api_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='coin',
            name='website',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='influncer',
            name='image_url',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='influncer',
            name='website',
            field=models.CharField(max_length=250),
        ),
    ]
