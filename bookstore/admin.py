from django.contrib import admin
from .models import Book, BookAuthor, BookTranslator, BookPublisher, Subject, Comment


class CommentInlines(admin.TabularInline):
    model = Comment
    fields = ('author', 'body', 'active')
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'book_author', 'status', 'owner', 'datetime_modified', 'active']
    ordering = ('-datetime_modified', )

    inlines = [
        CommentInlines
    ]


admin.site.register(BookAuthor)
admin.site.register(BookTranslator)
admin.site.register(BookPublisher)
admin.site.register(Subject)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['book', 'author', 'active']
    ordering = ('-datetime_created',)


