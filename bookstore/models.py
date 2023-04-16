from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class BookAuthor(models.Model):
    author_name = models.CharField(max_length=200, verbose_name=_('book author'))
    biography = models.TextField(verbose_name=_('biography'), blank=True)

    class Meta:
        verbose_name_plural = _('BookAuthors')

    def __str__(self):
        return self.author_name


class BookTranslator(models.Model):
    translator_name = models.CharField(max_length=200, verbose_name=_('translator name'))

    class Meta:
        verbose_name_plural = _('BookTranslators')

    def __str__(self):
        return self.translator_name


class BookPublisher(models.Model):
    publisher_name = models.CharField(max_length=200, verbose_name=_('publisher name'))
    short_description = models.CharField(max_length=500, blank=True, verbose_name=_('about publisher'))

    class Meta:
        verbose_name_plural = _('BookPublishers')

    def __str__(self):
        return self.publisher_name


class Subject(models.Model):
    subject = models.CharField(verbose_name=_('book subject'))

    class Meta:
        verbose_name_plural = _('Subjects')

    def __str__(self):
        return self.subject


class Book(models.Model):
    STATUS_CHOICES = (
        ('preparing', _('Preparing')),
        ('available', _('Available')),
        ('not available', _('Not Available')),

    )

    book_name = models.CharField(max_length=200, verbose_name=_('book name'))
    book_author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE, related_name='authors',
                                    verbose_name=_('book author'))
    book_publisher = models.ForeignKey(BookPublisher, on_delete=models.CASCADE, related_name='publishers',
                                       verbose_name=_('publisher name'))
    publication_year = models.PositiveIntegerField(verbose_name=_('publication year'))
    book_introduction = models.TextField(verbose_name=_('book introduction'))
    short_description = models.CharField(max_length=500, blank=True, verbose_name=_('short description'))
    book_price = models.PositiveIntegerField(verbose_name=_('book price'))
    book_pages = models.PositiveIntegerField(verbose_name=_('number of pages'))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subjects',
                                verbose_name=_('book subject'))

    status = models.CharField(choices=STATUS_CHOICES, max_length=13, verbose_name=_('status'))
    active = models.BooleanField(default=True, verbose_name=_('active status'))
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('book owner'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('creation date'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Modification date'))

    class Meta:
        verbose_name_plural = _('Books')

    def __str__(self):
        return f"book introduction: {self.book_name}, {self.book_author}, {self.subject}"
