# Generated by Django 4.2.6 on 2023-11-04 18:21

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('jumbotron_block', wagtail.blocks.StructBlock([('headline', wagtail.blocks.CharBlock(blank=True, form_classname='Title')), ('paragraph', wagtail.blocks.RichTextBlock(blank=True)), ('button_text', wagtail.blocks.CharBlock(blank=True, form_classname='Button Text')), ('bg_color', wagtail.blocks.ChoiceBlock(blank=True, choices=[('bg-body-tertiary', 'Tertiary'), ('Light', 'Dark')], label='Hintergrund Farbe', max_length=20)), ('page_link', wagtail.blocks.PageChooserBlock(help_text='Wählen Sie die verlinkte Seite aus', label='Seiten Verlinkung', required=False))])), ('marketing_block', wagtail.blocks.StructBlock([('subline', wagtail.blocks.CharBlock(blank=True, form_classname='Subline')), ('heading', wagtail.blocks.CharBlock(blank=True, form_classname='Title')), ('paragraph', wagtail.blocks.RichTextBlock(blank=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_align', wagtail.blocks.ChoiceBlock(blank=True, choices=[('last', 'Links'), ('first', 'Rechts')], label='Textausrichtung', max_length=20))])), ('cards_block', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('titel', wagtail.blocks.CharBlock(label='Titel', max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(label='Textbereich', max_length=200, required=True)), ('button_page', wagtail.blocks.PageChooserBlock(label='Seiten Verlinkung', required=False)), ('cta', wagtail.blocks.CharBlock(label='cta', max_length=40, required=True)), ('color_scheme', wagtail.blocks.ChoiceBlock(blank=True, choices=[('bg-body-tertiary', 'Light'), ('text-bg-dark', 'Dark')], label='Farbschema', max_length=20))])))]))], blank=True, use_json_field=True),
        ),
    ]
