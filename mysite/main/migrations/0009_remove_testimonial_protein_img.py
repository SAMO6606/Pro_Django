# Generated by Django 4.2.2 on 2023-06-09 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_testimonial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='protein_img',
        ),
    ]
