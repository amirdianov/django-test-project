# Generated by Django 4.1.1 on 2022-12-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_note_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_shared',
            field=models.BooleanField(default=False),
        ),
    ]
