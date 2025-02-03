from django.shortcuts import render,get_object_or_404
from rango.models import Category, Page
from django.urls import reverse
from rango.forms import CategoryForm, PageForm
from django.shortcuts import render, redirect 

def add_category(request):
    form = CategoryForm()
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
        else:
            print(form.errors)
    
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    category = get_object_or_404(Category, slug=category_name_slug)
    form = PageForm()
    
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.category = category
            page.views = 0
            page.save()
            return redirect(reverse('show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)

    return render(request, 'rango/add_page.html', {'form': form, 'category': category})



def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    category_list = Category.objects.order_by('-views')[:5]  
    liked_category_list = Category.objects.order_by('-likes')[:5]  
    page_list = Page.objects.order_by('-views')[:5]  
    
    context_dict = {
        'categories': category_list,
        'liked_categories': liked_category_list,  # Yeni eklendi
        'pages': page_list
    }
  
    return render(request, 'rango/index.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = get_object_or_404(Category, slug=category_name_slug)
        pages = Page.objects.filter(category=category).order_by('-views')

        context_dict['category'] = category
        context_dict['pages'] = pages
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

def test_media(request):  
    return render(request, 'rango/test_media.html')