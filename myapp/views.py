from django.shortcuts import render, redirect
from .models import *
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.forms import UserCreationForm 
from .forms import UserRegistration
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    categories = Category.objects.all()
    images = Image.objects.all().order_by('-date_posted')
    user = request.user
    paginator = Paginator(images, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {'categories': categories, 'user': user, 'page_obj': page_obj, 'images':images}
    return render(request, 'index.html', data)





def show_catergory(request, cid):
    categories = Category.objects.all()                     #fetching all categories
    
    cats = Category.objects.get(pk=cid)                     #for single category with primary key of it 

    images = Image.objects.filter(cat=cats)                 #filter image according to categories

    paginator = Paginator(images, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {'images': images, 'categories': categories , 'page_obj': page_obj}
    return render(request, 'index.html', data)


def about(request):
    return render(request, 'about.html')


class ImageUploadView(LoginRequiredMixin ,CreateView):
    model = Image
    fields = ['cat', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUploadView(LoginRequiredMixin ,CreateView):
    model = Category
    fields = ['title']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('image-upload')

    


def userreg(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserRegistration()
    return render(request, 'register.html', {'form':form})


class ImageDeleteView(LoginRequiredMixin ,DeleteView):
    model = Image
    success_url = '/'


@login_required
def like_post(request):
    user = request.user
    if request.method == "POST":
        image_id = request.POST.get('image_id')
        image_obj = Image.objects.get(id=image_id)

        if user in image_obj.liked.all():
            image_obj.liked.remove(user)
        else:
            image_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, image_id=image_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        
        like.save()

    return redirect('index')