from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True) # not required and can be empty

    # When you add fields to content_panels, it enables them to be edited on the Wagtail interface. 
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
    pass
