# Generated by Django 4.2.2 on 2023-06-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pro_Futter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='Image')),
                ('text', models.TextField(verbose_name='Text')),
            ],
        ),
    ]
