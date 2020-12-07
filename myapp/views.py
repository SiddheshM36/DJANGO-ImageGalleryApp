from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    

    data = {'images': images, 'categories': categories}
    return render(request, 'index.html', data)



def show_catergory(request, cid):
    categories = Category.objects.all()                     #fetching all categories
    
    cats = Category.objects.get(pk=cid)                     #for single category with primary key of it 

    images = Image.objects.filter(cat=cats)                 #filter image according to categories

    data = {'images': images, 'categories': categories}
    return render(request, 'showimg.html', data)


def about(request):
    return render(request, 'about.html')


