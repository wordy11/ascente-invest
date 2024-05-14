# Generated by Django 5.0.4 on 2024-05-11 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_transactions_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='token',
            field=models.CharField(choices=[('btc', 'btc'), ('eth', 'eth'), ('usdt', 'trc20/usdt')], default='btc', max_length=10),
        ),
    ]