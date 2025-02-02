from django.shortcuts import render,get_object_or_404
from rango.models import Category, Page

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    category_list = Category.objects.order_by('-views')[:5]  # En popüler 5 kategori
    liked_category_list = Category.objects.order_by('-likes')[:5]  # En çok beğenilen 5 kategori
    page_list = Page.objects.order_by('-views')[:5]  # En çok görüntülenen 5 sayfa
    
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