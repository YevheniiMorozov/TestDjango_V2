from django.contrib import admin
from .models import News, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date_create", "author")
    list_display_links = ("id", "author")
    search_fields = ("title", "author")

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "body", "created")
    list_display_links = ("post", "user", "body")
    search_fields = ("name", "post")


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentsAdmin)
