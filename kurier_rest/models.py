from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.utils import timezone


class Kurier(models.Model):
    ZIELONY = 1
    NIEBIESKI = 2
    CZERWONY = 3
    RODZAJE_KURIEROW = [
        (ZIELONY, 'Początkujący (Zielony)'),
        (NIEBIESKI, 'Średnio zaawansowany (Niebieski)'),
        (CZERWONY, 'Zaawansowany (Czerwony)')]

    uzytkownik = models.OneToOneField(User, on_delete=models.CASCADE)
    imie = models.CharField(max_length=400, verbose_name=u'Imie', blank=False, null=False)
    nazwisko = models.CharField(max_length=400, verbose_name=u'Nazwisko', blank=False, null=False)
    telefon = PhoneField(blank=True, help_text='Numer telefonu')
    typ = models.IntegerField(choices=RODZAJE_KURIEROW, verbose_name=u'Rodzaj kuriera', blank=False, null=False)

    class Meta:
        verbose_name = u'Kurier'
        verbose_name_plural = u'Kurierzy'

    def __str__(self):
        return self.uzytkownik.username


class Rower(models.Model):
    nazwa = models.CharField(max_length=400, verbose_name=u'Nazwa', blank=False, null=False)
    data_dodania = models.DateTimeField(default=timezone.now, verbose_name=u'Data dodania')

    class Meta:
        verbose_name = u'Rower'
        verbose_name_plural = u'Rowery'