# Generated by Django 3.1.6 on 2021-04-19 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_feature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat_feature.contact'),
        ),
    ]
