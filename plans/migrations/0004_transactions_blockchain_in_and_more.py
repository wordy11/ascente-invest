# Generated by Django 5.0.4 on 2024-05-12 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0003_wallet_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='blockchain_in',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='transactions',
            name='blockchain_out',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]