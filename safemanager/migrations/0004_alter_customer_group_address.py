# Generated by Django 4.0.4 on 2022-05-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safemanager', '0003_customer_group_customer_next_of_kin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_group',
            name='address',
            field=models.TextField(max_length=50),
        ),
    ]
