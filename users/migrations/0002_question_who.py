# Generated by Django 4.2.2 on 2023-06-11 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='who',
            field=models.ManyToManyField(to='users.candidate'),
        ),
    ]
