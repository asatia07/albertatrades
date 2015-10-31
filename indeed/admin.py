from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import Trade, UserProfile, QuerySearchHistory

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False

# Define a new User admin
class UserAdmin(UserAdmin):
	inlines = (UserProfileInline, )

class TradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'job_counts', 'modified']

class QuerySearchHistoryAdmin(admin.ModelAdmin):
    list_display = ['trade', 'user_id', 'location', 'created', 'modified']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Trade, TradeAdmin)
admin.site.register(QuerySearchHistory, QuerySearchHistoryAdmin)
