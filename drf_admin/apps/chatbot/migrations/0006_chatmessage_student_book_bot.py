# Generated by Django 2.2.27 on 2024-01-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0005_auto_20240120_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='student_book_bot',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
