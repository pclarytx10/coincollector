# Generated by Django 4.1.5 on 2023-02-05 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_coin_price_influncer_real_name_alter_coin_api_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='image_url',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
