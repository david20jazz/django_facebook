# Generated by Django 3.0.7 on 2020-06-17 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.CharField(default='', max_length=120),
        ),
    ]