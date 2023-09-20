from django.contrib import admin
from .models import PostModel, CommentModel, RecyclePost, RecycleComment, RelationPostModel, TagPostModel, PostOptionModel


@admin.register(TagPostModel)
class TagPostAdmin(admin.ModelAdmin):
    ...

@admin.register(PostOptionModel)
class PostOptionModel(admin.ModelAdmin):
    ...

@admin.register(RecyclePost)
class RecyclePostAdmin(admin.ModelAdmin):
    ...

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    ordering = ('-create_at', )
    search_fields = ('user', )
    list_filter = ('create_at',)
    raw_id_fields = ('user', )
    list_display = ('user', 'id', 'create_at', 'body', 'is_active')
    list_editable= ('is_active', )
    prepopulated_fields = {'slug': ('body', )}
    
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
    list_display = ['post', 'like', 'create_at']