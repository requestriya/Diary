# Generated by Django 3.0.7 on 2021-03-30 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210328_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
