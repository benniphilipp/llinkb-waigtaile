from django.db import models

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RichTextBlock


# Marketing Block
class MarketingBlock(blocks.StructBlock):
    subline = blocks.CharBlock(form_classname="Subline", blank=True)
    heading = blocks.CharBlock(form_classname="Title", blank=True)
    paragraph = blocks.RichTextBlock(blank=True)
    image = ImageChooserBlock(required=False)
    
    page_link = models.ForeignKey(
        Page,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Seiten Verlinkung",
        related_name='+',
    )
    
    text_align = blocks.ChoiceBlock(
        max_length=20,
        choices=[('last', 'Links'), ('first', 'Rechts')],
        blank=True,
        default='last',
        label='Textausrichtung',
    )

    class Meta:
        template = 'stream/marketing-text.html'
        icon = 'edit'
        label = "Marketing Block"
        
# Jumbotron
class JumbotronBlock(blocks.StructBlock):
    headline = blocks.CharBlock(form_classname="Title", blank=True)
    paragraph = blocks.RichTextBlock(blank=True)
    
    bg_color = blocks.ChoiceBlock(
        max_length=20,
        choices=[('bg-body-tertiary', 'Tertiary'), ('text-bg-dark', 'Dark')],
        blank=True,
        default='text-bg-dark',
        label='Hintergrund Farbe',
    )
    
    page_link = blocks.PageChooserBlock(
        required=False,
        help_text="Wählen Sie die verlinkte Seite aus",
        label="Seiten Verlinkung",
    )
    
    class Meta:
        template = 'stream/jumbotron.html'
        icon = 'edit'
        label = "Jumbotron"