from django.urls import path
from core.views import index, product_list_view, category_list_view, category_product_list_view, product_detail_view # vendow_list_view


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
    
    
]