from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Avg

class Book(models.Model):
    """
    書籍
    """

    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, verbose_name=_('書籍名稱'))
    description = models.TextField(blank=True, null=True, verbose_name=_('書籍簡介'))
    content = models.TextField(blank=True, null=True, verbose_name=_('書籍內容'))
    author = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('書籍作者'))
    publisher = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('書籍出版社'))
    publish_date = models.DateField(blank=True, null=True, verbose_name=_('書籍出版日期'))
    category = models.CharField(max_length=100,  blank=True, null=True, verbose_name=_('書籍分類'))
    difficulty = models.CharField(max_length=50,blank=True, null=True, verbose_name=_('書籍難度'))
    class Meta:
        verbose_name = _('書籍')
        verbose_name_plural = _('書籍')
        ordering = ['book_id']

    def __str__(self):
        return self.name

    def calculate_average_rating(self):
        """
        計算書籍的平均評分
        """
        ratings = self.ratings.all()
        if ratings.count() == 0:
            return None
        return ratings.aggregate(Avg('rating'))['rating__avg']
class BookRating(models.Model):
    """
    書籍評分
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings', verbose_name=_('書籍'))
    rating = models.DecimalField(max_digits=3, decimal_places=2, verbose_name=_('評分'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('創建時間'))

    class Meta:
        verbose_name = _('書籍評分')
        verbose_name_plural = _('書籍評分')

    def __str__(self):
        return f'{self.book.name} - {self.rating}'

