# Generated by Django 5.1.1 on 2024-10-05 13:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0003_user_offers_count_referral"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_referred",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="referral",
            name="offered_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="offered_users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="referral",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="referrals",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
