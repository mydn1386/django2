# actions = [delete_selected]
# @admin.action(description='حذف انتخاب شده‌ها')
# def delete_selected(modeladmin, request, queryset):
#     queryset.delete()

# actions = [delete_selected]
#
# from django.contrib import admin
# from .models import Post, Account


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author', 'status', 'published')
#     list_filter = ('status', 'created', 'updated', 'author')
#     search_fields = ('title', 'caption')
#     raw_id_fields = ('author',)
#     date_hierarchy = 'published'
#     ordering = ('status', '-published')
#     list_editable = ('status',)
#     prepopulated_fields = {'slug': ('title',)}
#     list_display_links = ('slug', 'title',)
#

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'user_first_name', 'user_last_name')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'

    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = 'First Name'

    def user_last_name(self, obj):
        return obj.user.last_name
    user_last_name.short_description = 'Last Name'

