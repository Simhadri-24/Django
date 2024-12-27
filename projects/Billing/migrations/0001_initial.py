# Generated by Django 5.1.2 on 2024-11-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=50)),
                ('empnumber', models.IntegerField()),
                ('designation', models.CharField(choices=[('Manager', 'Manager'), ('Supervisor', 'Supervisor'), ('Seller', 'Seller'), ('Cashier', 'Cashier'), ('Cleaner', 'Cleaner'), ('Security', 'Security')], max_length=25)),
                ('mnumber', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('categoty', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('mrp', models.IntegerField()),
                ('disper', models.IntegerField()),
            ],
        ),
    ]
