from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'pub_date')
    list_filter = ('cover_type', 'pub_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date', 'title')

admin.site.register(Book, BookAdmin)
