# Generated by Django 3.2.4 on 2021-07-11 10:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kurier_rest', '0002_rower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rower',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c3fff4d3-d95b-49ec-a69f-337491bf92ad'), editable=False, primary_key=True, serialize=False),
        ),
    ]
