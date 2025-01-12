# Generated by Django 2.2.27 on 2024-01-21 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0008_auto_20240121_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='student_book_bot',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='bot_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='chatbot.StudentBookBot', verbose_name='學生書籍機器人'),
            preserve_default=False,
        ),
    ]
