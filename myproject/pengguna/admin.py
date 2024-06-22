from django.contrib import admin
from .models import Author, Book, Member

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    search_fields = ('first_name', 'last_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'genre')
    search_fields = ('title', 'isbn')
    list_filter = ('author', 'genre')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth', 'join_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('join_date',)
