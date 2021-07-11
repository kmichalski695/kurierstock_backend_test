from django.contrib import admin
from .models import Kurier, Rower, Zmiana, UzycieRoweru


@admin.register(Kurier)
class KurierAdmin(admin.ModelAdmin):
    model = Kurier


@admin.register(Rower)
class RowerAdmin(admin.ModelAdmin):
    model = Rower

    fields = ('nazwa', 'data_dodania',)
    list_filter = ('nazwa', 'data_dodania')
    list_display = ('nazwa', 'data_dodania', 'qr_code')


class UzycieRoweruInLine(admin.StackedInline):
    model = UzycieRoweru
    extra = 0


@admin.register(Zmiana)
class ZmianaAdmin(admin.ModelAdmin):
    model = Zmiana

    fields = ('kurier', 'data_od', 'data_do')
    list_filter = ('kurier', 'data_od', 'data_do')
    list_display = ('data_od', 'data_do', 'kurier')
    inlines = [
        UzycieRoweruInLine,
    ]
