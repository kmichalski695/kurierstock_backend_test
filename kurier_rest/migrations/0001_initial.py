# Generated by Django 3.2.4 on 2021-07-10 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kurier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=400, verbose_name='Imie')),
                ('nazwisko', models.CharField(max_length=400, verbose_name='Nazwisko')),
                ('telefon', phone_field.models.PhoneField(blank=True, help_text='Numer telefonu', max_length=31)),
                ('typ', models.IntegerField(choices=[(1, 'Początkujący (Zielony)'), (2, 'Średnio zaawansowany (Niebieski)'), (3, 'Zaawansowany (Czerwony)')], verbose_name='Rodzaj kuriera')),
                ('uzytkownik', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kurier',
                'verbose_name_plural': 'Kurierzy',
            },
        ),
    ]