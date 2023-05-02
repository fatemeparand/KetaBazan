from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse


class BookAuthor(models.Model):
    author_name = models.CharField(max_length=200, unique=True, verbose_name=_('book author'))
    biography = models.TextField(verbose_name=_('biography'), blank=True)
    author_image = models.ImageField(verbose_name=_('author image'), upload_to='author_image/', blank=True)

    class Meta:
        verbose_name_plural = _('BookAuthors')

    def __str__(self):
        return self.author_name


class BookTranslator(models.Model):
    translator_name = models.CharField(max_length=200, unique=True, verbose_name=_('translator name'))

    class Meta:
        verbose_name_plural = _('BookTranslators')

    def __str__(self):
        return self.translator_name


class BookPublisher(models.Model):
    publisher_name = models.CharField(max_length=200, unique=True, verbose_name=_('publisher name'))
    short_description = models.CharField(max_length=500, blank=True, verbose_name=_('about publisher'))

    class Meta:
        verbose_name_plural = _('BookPublishers')

    def __str__(self):
        return self.publisher_name


class Subject(models.Model):
    subject = models.CharField(unique=True, verbose_name=_('book subject'))

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
    book_author = models.ForeignKey(
        BookAuthor,
        on_delete=models.CASCADE,
        related_name='authors',
        verbose_name=_('book author')
    )
    book_translator = models.ForeignKey(
        BookTranslator,
        on_delete=models.CASCADE,
        related_name='translator',
        blank=True,
        null=True,
        verbose_name=_('book translator')
    )
    book_publisher = models.ForeignKey(
        BookPublisher,
        on_delete=models.CASCADE,
        related_name='publishers',
        verbose_name=_('publisher name')
    )
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
    image = models.ImageField(upload_to='book image/', blank=True, verbose_name=_('book image'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('creation date'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Modification date'))

    class Meta:
        unique_together = ['book_name', 'book_author', 'book_translator', 'book_publisher']
        verbose_name_plural = _('Books')

    def __str__(self):
        return f"book introduction: {self.book_name}, {self.book_author}, {self.subject}"

    def get_absolute_url(self):
        return reverse('bookstore:book_detail', args={self.pk})


class Comment(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('book')
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('comment author')
    )
    body = models.TextField(verbose_name=_('comment text'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('time created'))
    active = models.BooleanField(default=True, verbose_name=_('active status'))

    class Meta:
        verbose_name_plural = _('Comments')
        ordering = ('-datetime_created',)

    def __str__(self):
        return f'{self.author}: {self.body}'

    def get_absolute_url(self):
        return reverse('bookstore:book_detail', args=[self.book.id])
