# Generated by Django 3.2.9 on 2021-12-06 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='title',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]