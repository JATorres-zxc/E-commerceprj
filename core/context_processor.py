from core.models import Address, Category, Vendor, Product, ProductImage, ProductReview, Wishlist, CartOrder, CartOrderItems



def default(request):
    categories = Category.objects.all()
    
    
    return {
        'categories':categories
    }