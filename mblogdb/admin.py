from django.contrib import admin

# Register your models here.

from mblogdb.models import *

class UserDetailAdmin(admin.ModelAdmin):
	list_display = ('user', 'nickname')
	search_fields = ('user', 'nickname')
admin.site.register(UserDetail, UserDetailAdmin)

class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'follow', 'date')
    search_fields = ('user', 'follow')
admin.site.register(Follow, FollowAdmin)
