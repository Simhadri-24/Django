# Generated by Django 5.1.2 on 2024-10-30 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rno', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('m1', models.IntegerField()),
                ('m2', models.IntegerField()),
                ('m3', models.IntegerField()),
                ('total', models.IntegerField(editable=False)),
                ('average', models.FloatField(editable=False)),
                ('result', models.CharField(editable=False, max_length=4)),
            ],
            options={
                'ordering': ['rno'],
            },
        ),
    ]
