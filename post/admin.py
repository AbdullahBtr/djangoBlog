from django.contrib import admin
from .models import Post
from .models import Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model=Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['author','title','created_on','body_text',]
    inlines=[
        CommentInline,
        
    ]

class CommentAdmin(admin.ModelAdmin):
    list_display=['author','text','created_on','post']


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)