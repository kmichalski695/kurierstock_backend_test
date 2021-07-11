# Generated by Django 3.2.4 on 2021-07-11 10:15

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kurier_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rower',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('ee1c0b42-98fd-4f98-9c40-f073904cb1fa'), editable=False, primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=400, verbose_name='Nazwa')),
                ('data_dodania', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data dodania')),
            ],
            options={
                'verbose_name': 'Rower',
                'verbose_name_plural': 'Rowery',
            },
        ),
    ]
