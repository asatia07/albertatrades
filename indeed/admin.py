from django.contrib import admin

# Register your models here.

from .models import Trade
from .models import SearchHistory

class TradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'job_counts', 'modified']

admin.site.register(Trade, TradeAdmin)


class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ['trade', 'user', 'created']

admin.site.register(SearchHistory, SearchHistoryAdmin)
