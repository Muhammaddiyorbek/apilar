# Generated by Django 4.2.2 on 2023-07-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apilarapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='content',
            field=models.TextField(default='text'),
            preserve_default=False,
        ),
    ]
