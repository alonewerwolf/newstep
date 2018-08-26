from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from newstep.models import Category
from newstep.models import Page
# Create your views here.

def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}


    return render(request, 'newstep/index.html', context_dict)

def category(request, category_name_slug):

    context_dict = {}

    try:

        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category = category.id)
 
        context_dict['pages'] = pages
        context_dict['category'] = category
        context_dict['category_name'] = category.name
      
    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['pages'] = None


    return render(request, 'newstep/category.html', context_dict)
 
    
