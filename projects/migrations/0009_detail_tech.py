# Generated by Django 3.0.3 on 2020-02-13 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20200213_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='tech',
            field=models.CharField(default='', max_length=200),
        ),
    ]