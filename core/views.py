from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import HttpRequest


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

    # products = Product.objects.filter(category=product.category)
    
    # p_image = product.product_image.all()
    
    context = {
        'product':product,
        # 'p_image':p_image,
        # 'products':products
    }
    
    return render(request, 'core/product-detail.html', context)


def search_view(request):
    query = request.GET.get('q')
    
    products = Product.objects.filter(title__icontains=query).order_by('-date')
    
    context = {
        'products':products,
        'query':query,
    }
    
    return render(request, 'core/search.html', context)


def add_to_cart(request):
    cart_product = {}

    required_params = ['id', 'title', 'qty', 'price']
    for param in required_params:
        if param not in request.GET:
            return JsonResponse({'error': f'Missing parameter: {param}'}, status=400)
        
    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
        'image':request.GET['image'],
        'pid':request.GET['pid'],
    }
    
    if 'cart_data_obj' in request.session:
        prod_id = request.GET.get("id")
        prod = Product.objects.get(id=prod_id)
        id = str(request.GET['id'])
        if str(request.GET.get('id')) in request.session.get('cart_data_obj', {}):
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]["qty"] = int(cart_product[str(request.GET['id'])]['qty'])
            cart_data[id]["price"] = cart_product[id]["price"]
            # cart_product[id]['price'] = prod.price
            # request.session['cart_data_obj'][id].update(cart_product[id])
            print("bruhhhhh")
            cart_data.update(cart_data)  
            request.session['cart_data_obj'] = cart_data
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
    else:
        request.session['cart_data_obj'] = cart_product 

    return JsonResponse({'data': request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})


def cart_view(request: HttpRequest):
    cart_total_amount = 0
    
    if 'cart_data_obj' in request.session:
        cart = request.session['cart_data_obj']
        for p_id, item in cart.items():
            cart_total_amount += int(item['qty']) * float(item['price'])
            
        return render(
            request, 
            'core/cart.html', 
            {'cart_data': request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
    else:
        # return render(request, 'core/cart.html', {'cart_data': '', 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
        messages.warning(request, 'Your cart is empty')
        return redirect('core:index')
# def cart_view(request):
#     cart_total_amount = 0
    
#     if 'cart_data_obj' in request.session:
#         for p_id, item in request.session['cart_data_obj'].items():
#             if item['price']:
#                 cart_total_amount += int(item['qty']) * float(item['price'])
#             else:
#                 item['price'] = '0'
#                 cart_total_amount += int(item['qty']) * float(item['price'])
            
#         return render(request, 'core/cart.html', {'cart_data': request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
#     else:
#         messages.warning(request, 'Your cart is empty')
#         return redirect('core:index')


def delete_item_from_cart(request):
    product_id = str(request.GET['id'])
    
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            del request.session['cart_data_obj'][product_id]
            request.session['cart_data_obj'] = cart_data
            
    cart_total_amount = 0
    
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
            
    
    context = render_to_string('core/async/cart-list.html', {'cart_data': request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
    
    return JsonResponse({'data':context, 'totalcartitems': len(request.session['cart_data_obj'])})

def update_from_cart(request):
    product_id = str(request.GET['id'])
    product_qty = request.GET['qty']
    
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = product_qty
            request.session['cart_data_obj'] = cart_data
            
    cart_total_amount = 0
    
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
            
    
    context = render_to_string('core/async/cart-list.html', {'cart_data': request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
    
    return JsonResponse({'data':context, 'totalcartitems': len(request.session['cart_data_obj'])})