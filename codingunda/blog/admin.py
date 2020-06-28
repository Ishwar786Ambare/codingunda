from django.contrib import admin
from .models import Post, Author, Categorie, subscribe

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Categorie)
admin.site.register(subscribe)
