from django.contrib import admin

# Register your models here.

from .models import Trade

class TradeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trade, TradeAdmin)
