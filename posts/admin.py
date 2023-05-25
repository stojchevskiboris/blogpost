from django.contrib import admin
from .models import Post, PostComment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author",)
    list_filter = ("title",)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# Register your models here.
admin.site.register(Post, PostAdmin)


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("post", "comment",)


admin.site.register(PostComment, PostCommentAdmin)
