from wagtail import blocks
from django.db import models
from wagtail.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RichTextBlock


# Marketing Block
class MarketingBlock(blocks.StructBlock):
    subline = blocks.CharBlock(form_classname="Subline", blank=True)
    heading = blocks.CharBlock(form_classname="Title", blank=True)
    paragraph = blocks.RichTextBlock(blank=True)
    image = ImageChooserBlock(required=False)
    
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
        label = "Text Group"