# Generated by Django 4.0.3 on 2022-04-24 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankingUI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
