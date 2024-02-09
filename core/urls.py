from django.urls import path
from core.views import index, product_list_view, category_list_view, category_product_list_view, product_detail_view, search_view, add_to_cart

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
    
    path('add-to-cart/', add_to_cart, name='add-to-cart')
]
