from django.contrib import admin

# Register your models here.

from .models import Trade
from .models import QuerySearchHistory

class TradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'job_counts', 'modified']

admin.site.register(Trade, TradeAdmin)

class QuerySearchHistoryAdmin(admin.ModelAdmin):
    list_display = ['trade', 'user_id', 'created']

admin.site.register(QuerySearchHistory, QuerySearchHistoryAdmin)
