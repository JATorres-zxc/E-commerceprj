from django.shortcuts import render
from django.http import HttpResponse
from core.models import Address, Category, Vendor, Product, ProductImage, ProductReview, Wishlist, CartOrder, CartOrderItems

# Create your views here.
def index(request):
    # products = Product.objects.all().order_by('-id')
    products = Product.objects.filter(featured=True, product_status='published').order_by('-id')
    context = {
        'products':products
    }
    return render(request, 'core/index.html', context)


def product_list_view(request):
    products = Product.objects.filter(product_status='published')
    context = {
        'products':products
    }
    return render(request, 'core/products-list.html', context)




def category_list_view(request):
    categories = Category.objects.all()
    # products = Product.objects.filter(featured=True, product_status='published').order_by('-id')
    context = {
        'categories':categories
    }
    return render(request, 'core/category-list.html', context)


def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status='published', category=category)
    
    context = {
        'category':category,
        'products':products
    }
    
    return render(request, 'core/category-products-list.html', context)


# def vendow_list_view(request):
#     vendor = Vendor.objects.all()
#     context = {
#         'vendor':vendor,
#     }
    
#     return render(request, 'core/vendor-list.html', context)

def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)

    context = {
        'product':product
    }
    
    return render(request, 'core/product-detail.html', context)