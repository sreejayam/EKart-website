from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, PacketSize
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.


def allProdCat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.all().filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator = Paginator(products_list, 4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, "category.html", {'category': c_page, 'products': products})


# def proDetail(request, c_slug, product_slug):
#     try:
#         product = Product.objects.get(category__slug=c_slug, slug=product_slug)
#     except Exception as e:
#         raise e
#     return render(request, 'product.html', {'product': product})
def about(request):
    return render(request,'about.html')


def proDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
<<<<<<< HEAD

    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})
=======
        packet_sizes = PacketSize.objects.filter(product=product)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product, 'packet_sizes': packet_sizes})
>>>>>>> d4c4eead28b5a93d352fb1a0951df745ce6bed89
