# Generated by Django 4.1.6 on 2023-02-11 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('date', models.DateTimeField()),
                ('message_text', models.TextField()),
                ('image_url', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=255)),
            ],
        ),
    ]
