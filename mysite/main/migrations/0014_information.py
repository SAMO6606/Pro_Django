# Generated by Django 4.2.2 on 2023-06-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_pro_futter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.TextField(verbose_name='Text 1')),
                ('text2', models.TextField(verbose_name='Text 2')),
                ('text3', models.TextField(verbose_name='Text 3')),
                ('text4', models.TextField(verbose_name='Text 4')),
                ('text5', models.TextField(verbose_name='Text 5')),
                ('text6', models.TextField(verbose_name='Text 6')),
            ],
        ),
    ]
