# Generated by Django 4.0.4 on 2022-05-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safemanager', '0004_alter_customer_group_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]