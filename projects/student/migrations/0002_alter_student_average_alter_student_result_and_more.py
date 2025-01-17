# Generated by Django 5.1.2 on 2024-10-30 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='average',
            field=models.FloatField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='result',
            field=models.CharField(editable=False, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='total',
            field=models.IntegerField(editable=False, null=True),
        ),
    ]
