# Generated by Django 4.1.7 on 2023-05-18 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='session_id',
            field=models.CharField(default='sample', max_length=20),
            preserve_default=False,
        ),
    ]
