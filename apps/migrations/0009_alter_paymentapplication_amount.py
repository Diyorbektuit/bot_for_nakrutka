# Generated by Django 5.1.1 on 2024-10-08 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0008_paymentapplication"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentapplication",
            name="amount",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
