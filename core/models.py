from django.db import models
from shortuuid.django_fields import ShortUUIDField # short ids
from django.utils.html import mark_safe
# from django.utils.safestring import mark_safe
from userauths.models import User
import uuid



STATUS_CHOICES = (
    ('process', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
)

STATUS = (
    ('draft', 'Draft'),
    ('disabled', 'Disabled'),
    ('rejected', 'Rejected'),
    ('in_review', 'In Review'),
    ('published', 'Published'),
)

RATING = (
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★'),
)

# Create your models here.

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)
    
class Category(models.Model):
    # category id
    # cid = models.UUIDField(unique=True, max_length=30, prefix='cat', alphabet='abcdefghijklmnopqrstuvwxyz1234567890')
    cid = models.UUIDField(unique=True, default=uuid.uuid4, editable=True)
    title = models.CharField(max_length=100, default='apparel')  # for title, heading etc
    image = models.ImageField(upload_to='category',default='category.jpg')
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
class Tags(models.Model):
    pass

class Vendor(models.Model):
    #vendor id
    # vid = models.UUIDField(unique=True, length=10, max_length = 30, prefix='ven', alphabet='abcdefghijklmnopqrstuvwxyz1234567890')
    vid = models.UUIDField(unique=True, default=uuid.uuid4, editable=True)

    title = models.CharField(max_length=100, default='something') # for title, heading etc
    image = models.ImageField(upload_to=user_directory_path,default='vendor.jpg')
    description = models.TextField(null=True, blank=True, default='vendor')
    
    address = models.CharField(max_length=100, default='123 A Street, PH')
    contact = models.CharField(max_length=100, default='123 456 789')
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default='100')
    authentic_rating = models.CharField(max_length=100, default='100')
    days_return = models.CharField(max_length=100, default='100')
    warranty_period = models.CharField(max_length=100, default='100')

        
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True, default=None)
    
    class Meta:
        verbose_name_plural = 'Vendor'
    
    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    #prodjuct id
    # pid = models.UUIDField(unique=True, length=10, max_length = 30, alphabet='abcdefghijklmnopqrstuvwxyz1234567890')
    pid = models.UUIDField(unique=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, null=True,default= None)
    
    title = models.CharField(max_length=100, default='something') # for title, heading etc
    image = models.ImageField(upload_to=user_directory_path,default='product.jpg')
    description = models.TextField(null=True, blank=True, default='product')
    price = models.DecimalField(max_digits=9, decimal_places=2, default='0.00')
    old_price = models.DecimalField(max_digits=9, decimal_places=2, default='1.00')
    specifications = models.TextField(null=True, blank=True, default='specs')
    # tags = models.ForeignKey(Tags, on_delete=models.SET_DEFAULT, null=True, default=None)
    type = models.CharField(max_length=100, default='something', null=True, blank=True) # for title, heading etc
    stock_count = models.CharField(max_length=100, default='0', null=True, blank=True)
    
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_DEFAULT, null=True,default= None)
    product_status = models.CharField(choices=STATUS, max_length=10, default='in_review')
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    # sku = models.UUIDField(unique=True, length=10, max_length = 30, prefix="sku", alphabet='1234567890')
    sku = models.UUIDField(unique=True, default=uuid.uuid4, editable=True)

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products'
    
    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = ((self.old_price - self.price) / self.old_price) * 100
        return new_price
    
class ProductImage(models.Model):
    images = models.ImageField(upload_to='product-images', default='product.jpg')
    product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, null=True, default=None)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Product Images'
        
        
        




class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, default='0.00')
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICES, max_length=30, default='processing')

    class Meta:
        verbose_name_plural = 'Cart Order'

class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=100)
    product_status = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9, decimal_places=2, default='0.00')
    total = models.DecimalField(max_digits=9, decimal_places=2, default='0.00')

    class Meta:
        verbose_name_plural = 'Cart Order Items'
        
    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))










class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, null=True, default=None)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default = None)
    date = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Product Reviews'
    
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True, default =None)
    product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, null=True, default =None)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Wishlist'
    
    def __str__(self):
        return self.product.title
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True, default=None)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Address'
