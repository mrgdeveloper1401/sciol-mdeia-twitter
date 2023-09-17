from django.contrib import admin
from .models import PostModel, CommentModel, RecyclePost, RecycleComment, RelationPostModel, TagPostModel


@admin.register(TagPostModel)
class TagPostAdmin(admin.ModelAdmin):
    ...

@admin.register(RecyclePost)
class RecyclePostAdmin(admin.ModelAdmin):
    ...

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    ordering = ('-create_at', )
    # readonly_fields = ('update_at', )
    prepopulated_fields = {'slug': ('body', )}
    search_fields = ('user', )
    list_filter = ('create_at',)
    raw_id_fields = ('user', )
    list_display = ('user', 'location', 'id', 'create_at', 'body', 'is_active')
    list_editable= ('is_active', )
    
    
@admin.register(RecycleComment)
class RecycleCommentAdmin(admin.ModelAdmin):
    ...

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'body', 'create_at', 'is_reply')
    list_filter = ('create_at', 'user')
    search_fields = ('body', 'reply', )
    raw_id_fields = ('user', )


@admin.register(RelationPostModel)
class RelationPostAdmin(admin.ModelAdmin):
    list_display = ['post', 'like', 'dislike', 'create_at']