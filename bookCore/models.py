from django.db import models
from django.utils.translation import ugettext as _
from users.models import UserProfile
from tag.models import Tag
from questionnaire.models import Questionnaire

# Create your models here.


types = (('sell', _('sell')),
         ('buy', _('buy')))


class Book(models.Model):
    """
        Book information model
    """

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='users_books', verbose_name=_('user'),
                             help_text=_('user of book'))
    title = models.CharField(max_length=255, verbose_name=_('title'), help_text=_('title of book'))
    # tag with classification author
    authors = models.ManyToManyField(Tag, related_name='authored_books', verbose_name=_('author'),
                                     help_text=_('author(s) of book'))
    # tag with classification translator
    translators = models.ManyToManyField(Tag, related_name='translated_books', verbose_name=_('translator'),
                                         help_text=_('translator(s) of book'), blank=True)
    # tag with classification publisher
    publisher = models.ForeignKey(Tag, related_name='published_books', on_delete=models.CASCADE,
                                  verbose_name=_('publisher'), help_text=_('publisher of book'))
    edition = models.PositiveIntegerField(verbose_name=_('edition'), help_text=_('edition of book'), blank=True,
                                          null=True)
    page_count = models.PositiveIntegerField(verbose_name=_('page count'), help_text=_('page count of book'),
                                             blank=True, null=True)
    # has image.all()

    volume = models.PositiveIntegerField(verbose_name=_('volume'), help_text=_('volume of book'), blank=True, null=True)
    publication_year = models.PositiveIntegerField(verbose_name=_('publication_year'),
                                                   help_text=_('publication year of book'), blank=True, null=True)
    original_price = models.PositiveIntegerField(verbose_name=_('original price'),
                                                 help_text=_('original price of book'))
    price = models.PositiveIntegerField(verbose_name=_(' price'),
                                        help_text=_('price of book'))
    type = models.CharField(max_length=5, choices=types, default='sell')
    # tag with classification ALL
    category = models.ManyToManyField(Tag, related_name='category_books', verbose_name=_('category'),
                                      help_text=_('category of book'))
    quality = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, verbose_name=_('quality'),
                                help_text=_('quality of book'))
    is_verified = models.BooleanField(default=False, verbose_name=_('is verified'),
                                      help_text=_('is the book verified or not'))

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name=_('image'), help_text=_('image of book'))
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='image', verbose_name=_('book'),
                             help_text=_('book images'))


class BookRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='request', verbose_name=_('book'),
                             help_text=_('book requests'))
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_requested',
                             verbose_name=_('user'), help_text=_('user requested'))
    is_selected = models.BooleanField(default=False, verbose_name=_('is selected'), help_text=_('is user selected'))
