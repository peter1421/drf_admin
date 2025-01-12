# Generated by Django 2.2.27 on 2024-01-28 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20240120_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, choices=[('fiction', '小說'), ('nonfiction', '非小說'), ('science', '科學'), ('history', '歷史'), ('story', '故事'), ('humansocial', '人社'), ('other', '其他')], max_length=100, null=True, verbose_name='書籍分類'),
        ),
        migrations.AlterField(
            model_name='book',
            name='difficulty',
            field=models.CharField(blank=True, choices=[('picture', '繪本'), ('bridge', '中等'), ('elementary', '初階文字書'), ('intermediate', '中階文字書'), ('advanced', '高階文字書')], max_length=50, null=True, verbose_name='書籍難度'),
        ),
    ]
