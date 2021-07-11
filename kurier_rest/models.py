import uuid
from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.utils import timezone
from django.utils.html import format_html, mark_safe
from django.shortcuts import render
import qrcode
import qrcode.image.svg
from io import BytesIO



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
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    nazwa = models.CharField(max_length=400, verbose_name=u'Nazwa', blank=False, null=False)
    data_dodania = models.DateTimeField(default=timezone.now, verbose_name=u'Data dodania')

    @property
    def qr_code(self):
        if self.id is None:
            return format_html('<div>brak</div>')
        else:
            factory = qrcode.image.svg.SvgImage
            img = qrcode.make(self.ID, image_factory=factory, box_size=20)
            stream = BytesIO()
            img.save(stream)
            xml = stream.getvalue().decode().replace('<?xml version=\'1.0\' encoding=\'UTF-8\'?>','')
            return format_html("<div style=\"background-color:white;\">{}</div>", mark_safe(xml))

    class Meta:
        verbose_name = u'Rower'
        verbose_name_plural = u'Rowery'



