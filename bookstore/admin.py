from django.contrib import admin
from .models import Book, BookAuthor, BookTranslator, BookPublisher, Subject


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'book_author', 'status', 'owner', 'datetime_modified', 'active']
    ordering = ('-datetime_modified', )


admin.site.register(BookAuthor)
admin.site.register(BookTranslator)
admin.site.register(BookPublisher)
admin.site.register(Subject)


