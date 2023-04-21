from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#to give state choices to the user
STATE_CHOICES = (
   ('Maharashtra','Maharashtra'),
   ('Bihar','Bihar'),
   ('Uttar Pradesh','Uttar Pradesh'),
   ('Telangana','Telangana'),
   ('Karnataka','Karnataka'),
   ('Kerala','Kerala'),
   ('Madhya Pradesh','Madhya Pradesh'),
   ('Orissa','Orissa'),
   ('Gujrat','Gujrat'),
   ('Rajasthan','Rajasthan'),
   ('Haryana','Haryana'),
   ('Punjab','Punjab'),
   ('Himachal Pradesh','Himachal Pradesh')
)

CATEGORY_CHOICES = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear')

)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality =models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return f'{self.id}'
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category =models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return str(self.id)
    

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way ','On the Way'),
    ('Delivered','Delivered'),
    ('Cancelled','Cancelled')

)

class Order_Placed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DateTimeField(auto_now_add=True)
    ordered_date = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATE_CHOICES, default='Pending')