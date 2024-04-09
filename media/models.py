from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField

class Media(models.Model):
    class FyleType(models.TextChoices):
        IMAGE = 'image', _('image')
        VIDEO = 'video', _('video')
        DOCUMENT = 'document', _('document')
        GIF = 'gid', _('gif')
        OTHER = 'other', _('other')
    file = models.FileField(upload_to='media/', verbose_name=_('File'),
                            validators=[FileExtensionValidator(
                                allowed_extensions=['jpg', 'jpeg', 'svg', 'png', 'webp',
                                                    'mp4', 'mpeg4', 'avi', 'mov', 'mkv',
                                                    'doc', 'docx', 'pdf', 'gif']
                            )])
    file_type = models.CharField(max_length=20,
                                 verbose_name=_('File Type'),
                                 choices=FyleType.choices)
    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Medias')

    def __str__(self):
        return f'id: {self.id}| Name: {self.file.name.split('/')[-1]}'

    def clean(self):
        if self.file_type not in self.FyleType.values:
            raise ValidationError(_('Invalid File Type'))
        elif self.file_type == self.FyleType.IMAGE:
            if self.file.name.split('/')[-1] not in ['jpg', 'jpeg', 'svg', 'png', 'webp']:
                raise ValidationError(_('Invalid Image File'))
        elif self.file_type == self.FyleType.VIDEO:
            if self.file.name.split('/')[-1] not in ['mp4', 'mpeg4', 'avi', 'mov', 'mkv']:
                raise ValidationError(_('Invalid Video File'))
        elif self.file_type == self.FyleType.DOCUMENT:
            if self.file.name.split('/')[-1] not in ['doc', 'docx', 'pdf', 'gif']:
                raise ValidationError(_('Invalid Document File'))

class Settings(models.Model):
    main_text = RichTextField(_('main text'))
    main_phone_number = models.CharField(max_length=20, verbose_name=_('main_phone_number'))
    main_image = models.ForeignKey(Media, verbose_name=_('main image'), on_delete=models.CASCADE,
                                   related_name='main_image')
    blog_images = models.ForeignKey(Media, verbose_name=_('blog image'), on_delete=models.CASCADE,
                                    related_name='blog_images')
    other_images = models.ForeignKey(Media, verbose_name=_('Other images'), on_delete=models.CASCADE,
                                     related_name='other_images')

    class Meta:
        verbose_name = _('Settings')
        verbose_name_plural = _('Settings')

    def __str__(self):
        return self.main_text


