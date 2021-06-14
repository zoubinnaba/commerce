# Generated by Django 2.2 on 2021-04-08 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=20),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid_price', to='auctions.Bids'),
        ),
    ]