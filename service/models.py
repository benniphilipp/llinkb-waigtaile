from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.api import APIField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

from stream.blocks import MarketingBlock, JumbotronBlock, CardsBlock, TextBlock

class ServidePage(Page):
    
    template = "service/service_page.html"
    
    headline = models.CharField(blank=True, max_length=250)
    text = RichTextField(blank=True, features=['bold', 'italic'])
    cta_text = models.CharField(blank=True, max_length=90, verbose_name="Button Text")
    
    # Seiten- und Blogbeitragsfelder
    page_link = models.ForeignKey(
        Page,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Seiten Verlinkung",
        related_name='+',
    )

    ''' Content Pages '''
    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        FieldPanel('text'),
    ]
    
    '''@Todo StreamField'''
    content = StreamField([
        ('jumbotron_block', JumbotronBlock()),
        ('marketing_block', MarketingBlock()),
        ('cards_block', CardsBlock()),
        ('text_block', TextBlock()),
    ], 
    blank=True,           
    use_json_field=True)
    
    content_stream = Page.content_panels + [
            FieldPanel('content'),
    ]
    
    ''' Admin Tab '''
    edit_handler = TabbedInterface([
        ObjectList(content_stream, heading='Content'),
        ObjectList(content_panels, heading='Header'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Service Pages"