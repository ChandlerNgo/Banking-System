# Generated by Django 4.0.3 on 2022-04-16 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin_number', models.IntegerField()),
                ('username', models.CharField(max_length=30)),
                ('password', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_withdrawal', models.BooleanField()),
                ('amount', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankingUI.bankinfo')),
            ],
        ),
        migrations.AddField(
            model_name='bankinfo',
            name='customer_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankingUI.customer'),
        ),
    ]