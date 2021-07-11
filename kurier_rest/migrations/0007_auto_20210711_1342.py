# Generated by Django 3.2.4 on 2021-07-11 13:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kurier_rest', '0006_alter_rower_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rower',
            name='id',
        ),
        migrations.AddField(
            model_name='rower',
            name='ID',
            field=models.UUIDField(default=uuid.UUID('2c90b476-942b-46fe-b49c-ebe598807725'), editable=False, primary_key=True, serialize=False),
        ),
    ]
