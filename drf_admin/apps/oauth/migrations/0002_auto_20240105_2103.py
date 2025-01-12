# Generated by Django 2.2.27 on 2024-01-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', '男性'), ('female', '女性'), ('other', '其他')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.CharField(blank=True, default=None, max_length=11, null=True, unique=True, verbose_name='手機號碼'),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='真實姓名'),
        ),
    ]
