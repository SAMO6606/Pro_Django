# Generated by Django 4.2.2 on 2023-06-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_protein_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='About text')),
                ('button_name', models.CharField(max_length=30, verbose_name='Button Name')),
                ('image', models.ImageField(upload_to='images', verbose_name='Image')),
            ],
        ),
    ]
