from django.contrib import admin
from .models import Kurier, Rower


@admin.register(Kurier)
class KurierAdmin(admin.ModelAdmin):
    model = Kurier

@admin.register(Rower)
class RowerAdmin(admin.ModelAdmin):
    model = Rower

    fields = ( 'nazwa',  'data_dodania', )
    list_filter = ('nazwa', 'data_dodania')
    list_display = ('nazwa', 'data_dodania', 'qr_code')