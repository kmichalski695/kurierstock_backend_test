from django.contrib import admin
from django.utils.html import format_html
from .models import Kurier, Rower


@admin.register(Kurier)
class KurierAdmin(admin.ModelAdmin):
    model = Kurier

@admin.register(Rower)
class RowAdmin(admin.ModelAdmin):
    model = Rower