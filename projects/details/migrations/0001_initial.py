# Generated by Django 4.2.16 on 2024-10-27 15:41

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
                ('name', models.CharField(max_length=150)),
                ('rno', models.IntegerField(default=True)),
                ('m1', models.IntegerField(default=True)),
                ('m2', models.IntegerField(default=True)),
                ('m3', models.IntegerField(default=True)),
                ('m4', models.IntegerField(default=True)),
            ],
        ),
    ]