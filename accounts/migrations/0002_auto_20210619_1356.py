# Generated by Django 3.2.4 on 2021-06-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_table',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='register_table',
            name='age',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='register_table',
            name='city',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
