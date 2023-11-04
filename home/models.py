from django.db import models

from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, ObjectList, TabbedInterface
from wagtail.models import Page

from stream.blocks import MarketingBlock

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
    
    # StreamField
    content = StreamField([
        ('marketing_block', MarketingBlock()),
    ], 
    blank=True,           
    use_json_field=True)
    
    content_stream = Page.content_panels + [
        FieldPanel('content'),
    ]
    
    # Admin Tabs
    edit_handler = TabbedInterface([
        ObjectList(content_stream, heading='Content'),
        ObjectList(content_panels, heading='Header'),
        ObjectList(Page.promote_panels, heading='Promotional'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])