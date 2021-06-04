from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel

class AuthorPage(Page):
    name = models.CharField(max_length=250)
    intro = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('intro'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
