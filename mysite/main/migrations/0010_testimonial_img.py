# Generated by Django 4.2.2 on 2023-06-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_testimonial_protein_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protein_img', models.ImageField(upload_to='images', verbose_name='Protein Image')),
            ],
        ),
    ]
