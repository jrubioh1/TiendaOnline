from django.contrib import admin
from Blog.models import Categoria, Post

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields= ('updated','created')


class PostAdmin(admin.ModelAdmin):
    readonly_fields= ('updated','created')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)