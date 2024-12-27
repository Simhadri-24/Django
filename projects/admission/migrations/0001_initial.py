# Generated by Django 5.1.2 on 2024-10-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.IntegerField()),
                ('m1', models.IntegerField()),
                ('m2', models.IntegerField()),
                ('m3', models.IntegerField()),
                ('m4', models.IntegerField()),
                ('m5', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('mno', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]