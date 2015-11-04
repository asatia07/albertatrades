from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db.models import Q
# Register your models here.

from .models import Trade, UserProfile, UserSearchHistory

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False

# Define a new User admin
class UserAdmin(UserAdmin):
	inlines = (UserProfileInline, )

class TradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'job_counts', 'modified']
    
    def get_queryset(self, request):
        qs = super(TradeAdmin, self).get_queryset(request)
        return qs.exclude((Q(name__isnull=True) | Q(name__exact='')) & (Q(query__isnull=True) | Q(query__exact='')))

class UserSearchHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'query', 'location', 'date_time']

    def get_queryset(self, request):
        qs = super(UserSearchHistoryAdmin, self).get_queryset(request)
        return qs.exclude(Q(query__isnull=True) | Q(query__exact='')).order_by('-id')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Trade, TradeAdmin)
admin.site.register(UserSearchHistory, UserSearchHistoryAdmin)
