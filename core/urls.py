from django.urls import path
from core.views import index, product_list_view, category_list_view, category_product_list_view, product_detail_view, search_view, add_to_cart, cart_view, delete_item_from_cart, update_from_cart, checkout_view, checkout_process, clear_cart

app_name = 'core'

urlpatterns = [
    # home page
    path('', index, name='index'),
    path('products/', product_list_view, name='product-list'), 
    path('product/<pid>', product_detail_view, name='product-detail'), 
    
    # category page
    path('category/', category_list_view, name='category-list'),
    path('category/<cid>/', category_product_list_view, name='category-product-list'),
    
    # vendor page
    # path('vendors/', vendow_list_view, name='vendor-list' ),
    
    path('search/', search_view, name='search'),
    
    # add to cart function only
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    
    #add to cart page 
    path('cart/', cart_view, name='cart'),
    
    #delete item from cart function only
    path("delete-from-cart/", delete_item_from_cart, name="delete-from-cart"),
    
    # update cart function
    path('update-cart/', update_from_cart, name='update-cart'),
    
    # checkout page
    path('checkout/', checkout_view, name='checkout'),
    
    # proceed to checkout   
    path('checkout_process/', checkout_process, name='checkout_process'),
    
    # clear cart
    path('clear-cart/', clear_cart, name='clear_cart'),
]
