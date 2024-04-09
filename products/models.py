from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from media.models import Media


class Category(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    price = models.IntegerField(_('price'), default=0)
    discount = models.IntegerField(_('discount'), default=0)
    short_desc = models.TextField(_('short description'))
    desc = RichTextField(_('description'))
    product_image = models.ForeignKey(Media, verbose_name=_('product image'),
                                      on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=_('category'),
                                 on_delete=models.CASCADE)
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Products,
                                verbose_name=_('product'),
                                on_delete=models.CASCADE)
    image = models.ForeignKey(Media,
                              verbose_name=_('image'),
                              on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')

    def __str__(self):
        return self.product





