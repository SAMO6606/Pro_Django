from django.db import models

# Create your models here.

class Tittle(models.Model):
    tittle_name = models.CharField('Tittle Name', max_length=30)

class Content(models.Model):
    content1 = models.CharField('content1',max_length=30)
    content2 = models.CharField('content2',max_length=30)
    content3 = models.CharField('content3',max_length=30)
    content4 = models.CharField('content4',max_length=30)
    menu_icon = models.ImageField('Menu Icon', upload_to='images')

class Header(models.Model):
    logo = models.ImageField('Header logo', upload_to='images')
    name1 = models.CharField('name1', max_length=30)
    name2 = models.CharField('name2', max_length=30)
    image = models.ImageField('Header image', upload_to='images')
    button_name1 = models.CharField('Button name 1', max_length=30)
    button_name2 = models.CharField('Button name 2', max_length=30)

class Protein(models.Model):
    image = models.ImageField('Protein image', upload_to='images')
    price = models.IntegerField('Protein price')
    protein_type = models.CharField('Protein Type', max_length=30)
    button_name = models.CharField('button name', max_length=30)

class About(models.Model):
    text = models.TextField('About text')
    button_name = models.CharField('Button Name', max_length=30)
    image = models.ImageField('Image', upload_to='images')

class Growyhing(models.Model):
    button_name = models.CharField('Button Name', max_length=30)
    image = models.ImageField('Image', upload_to='images')


class Testimonial(models.Model):
    carusel_img = models.ImageField('Carusel Image', upload_to='images')
    carusel_name = models.CharField('Carusel Name', max_length=30)
    text = models.TextField('Text')

class Testimonial_img(models.Model):
    protein_img = models.ImageField('Protein Image', upload_to='images')


class Request(models.Model):
    full_name = models.CharField('Full Name', max_length=30)
    email = models.EmailField('Email')
    phone_number = models.CharField('Phone number', max_length=30)
    message = models.TextField('Message')


class Contact(models.Model):
    phone_number = models.CharField('Phone Number', max_length=60)
    location = models.CharField('Location', max_length=60)
    gmail = models.EmailField('Gmail')

class Pro_Futter(models.Model):
    image = models.ImageField('Image', upload_to='images')
    text = models.TextField('Text')

class Information(models.Model):
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    text3 = models.TextField('Text 3')
    text4 = models.TextField('Text 4')
    text5 = models.TextField('Text 5')
    text6 = models.TextField('Text 6')


class Helpful(models.Model):
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    text3 = models.TextField('Text 3')
    text4 = models.TextField('Text 4')
    text5 = models.TextField('Text 5')
    text6 = models.TextField('Text 6')

class Supported(models.Model):
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    text3 = models.TextField('Text 3')
    text4 = models.TextField('Text 4')
    text5 = models.TextField('Text 5')
    text6 = models.TextField('Text 6')

class Futter_Name(models.Model):
    name1 = models.CharField('Name1', max_length=30)
    name2 = models.CharField('Name2', max_length=30)
