# Generated by Django 4.2.6 on 2023-11-08 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'staudent_tbl',
            },
        ),
    ]
