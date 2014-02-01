from django.contrib import admin

# Register your models here.

from mblogdb.models import UserDetail

class UserDetailAdmin(admin.ModelAdmin):
	list_display = ('user', 'nickname')
	search_fields = ('user', 'nickname')

admin.site.register(UserDetail, UserDetailAdmin)
