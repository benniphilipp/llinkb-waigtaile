from django.db import models

from wagtail.admin.panels import FieldPanel, ObjectList, TabbedInterface
from wagtail.models import Page

class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1
    
    # Hero Homepage
    headline = models.CharField(blank=True, max_length=350, verbose_name="Überschrift")
    subline = models.CharField(blank=True, max_length=350, verbose_name="Unterzeile")

    # Hero Fields
    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        FieldPanel('subline'),
    ]
    
    # Admin Tabs
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Header'),
        ObjectList(Page.promote_panels, heading='Promotional'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])