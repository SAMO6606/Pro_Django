from django.shortcuts import render, redirect
from .models import Tittle,Content,Header,Protein,About,Growyhing,Testimonial,Testimonial_img,Request,Contact,Pro_Futter,Information,Helpful,Supported,Futter_Name
from .forms import RequestForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            Request.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = RequestForm()
    tittle = Tittle.objects.all()[0]
    content = Content.objects.all()[0]
    header = Header.objects.all()[0]
    protein_list = Protein.objects.all()
    about = About.objects.all()[0]
    growyhing = Growyhing.objects.all()[0]
    testimonial = Testimonial.objects.all()
    testimonial_img = Testimonial_img.objects.all()[0]
    contact = Contact.objects.all()[0]
    pro_futter = Pro_Futter.objects.all()[0]
    information = Information.objects.all()[0]
    helpful = Helpful.objects.all()[0]
    supported = Supported.objects.all()[0]
    futter_name = Futter_Name.objects.all()[0]
    return render(request,'main/index.html',context={
        'tittle':tittle,
        'content':content,
        'header':header,
        'protein_list':protein_list,
        'about':about,
        'growyhing':growyhing,
        'testimonial_img':testimonial_img,
        'testimonial':testimonial,
        'form':form,
        'contact':contact,
        'pro_futter':pro_futter,
        'information':information,
        'helpful':helpful,
        'supported':supported,
        'futter_name':futter_name
    })