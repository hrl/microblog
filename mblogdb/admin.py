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

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'repo', 'body', 'encoded_body', 'date', 'is_active')
    search_fields = ('id', 'user', 'body')
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'reco', 'body', 'encoded_body', 'date', 'is_active')
    search_fields = ('id', 'user', 'body')
admin.site.register(Comment, CommentAdmin)

class InformPoolAdmin(admin.ModelAdmin):
    list_display = ('user', 'inform_type', 'body', 'date')
    search_fields = ('user', 'inform_type')
admin.site.register(InformPool, InformPoolAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
admin.site.register(Topic, TopicAdmin)

