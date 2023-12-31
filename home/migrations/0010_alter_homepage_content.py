# Generated by Django 4.2.6 on 2023-11-04 15:46

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('marketing_block', wagtail.blocks.StructBlock([('subline', wagtail.blocks.CharBlock(blank=True, form_classname='Subline')), ('heading', wagtail.blocks.CharBlock(blank=True, form_classname='Title')), ('paragraph', wagtail.blocks.RichTextBlock(blank=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_align', wagtail.blocks.ChoiceBlock(blank=True, choices=[('left', 'Links'), ('right', 'Rechts')], label='Textausrichtung', max_length=20))]))], blank=True, use_json_field=True),
        ),
    ]
