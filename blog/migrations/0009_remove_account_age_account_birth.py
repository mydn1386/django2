# Generated by Django 4.2.13 on 2024-06-19 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_account_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='age',
        ),
        migrations.AddField(
            model_name='account',
            name='birth',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
