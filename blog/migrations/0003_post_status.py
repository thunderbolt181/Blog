# Generated by Django 3.0.4 on 2020-04-25 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200424_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.TextField(blank=True, max_length=20),
        ),
    ]
