# Generated by Django 2.2.27 on 2024-01-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0004_auto_20240105_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(blank=True, choices=[('男性', '男性'), ('女性', '女性'), ('其他', '其他')], default=None, max_length=11, null=True, verbose_name='性別'),
        ),
    ]
