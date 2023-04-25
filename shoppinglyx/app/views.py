from django.shortcuts import render
from .models import Product, Customer, Order_Placed, Cart
from django.views import View
from .forms import CustomerRegistrationForm
from django.contrib import messages
# def home(request):
#  return render( request, 'app/home.html')

class ProductView(View):
    def get(self, request):
     topwears = Product.objects.filter(category='TW')
     bottomwears = Product.objects.filter(category='BW')
     mobiles = Product.objects.filter(category='M')
     laptops = Product.objects.filter(category='L')
     print(bottomwears)
     return render(request, template_name='app/home.html', context={'topwear':topwears, 
                        'bottomwears':bottomwears,
                        'mobiles':mobiles,
                        'laptops':laptops  })
     
     
class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render(request, template_name='app/productdetail.html',context={'product':product})
 

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
 if data == None:
    mobiles = Product.objects.filter(category = 'M')

 elif data =='Redmi' or data =='Samsung' or data =='Apple':
    print(data)
    mobiles = Product.objects.filter(category = 'M').filter(brand=data)
    print(mobiles)

 elif data == 'below':
    mobiles = Product.objects.filter(category = 'M').filter(discounted_price__lte=10000)

 elif data == 'above':
    mobiles = Product.objects.filter(category = 'M').filter(discounted_price__gte=20000)
 return render(request, 'app/mobile.html', context={'mobiles': mobiles})


def laptop(request, data=None):
  if data == None:
    laptop = Product.objects.filter(category= 'L')

  elif data=='dell' or data=='hp' or data=='HP' or data=='apple' or data=='Apple':
    print(data)
    laptop = Product.objects.filter(category='L').filter(brand=data)
    print(laptop)

  elif data == 'below':
    laptop = Product.objects.filter(category = 'L').filter(discounted_price__lte=40000)

  elif data == 'above':
    laptop = Product.objects.filter(category = 'L').filter(discounted_price__gte=40000)

  return render(request, 'app/laptop.html', context={'laptops': laptop})


def topwear(request, data=None):
  print(data)
  if data==None:
    topwear = Product.objects.filter(category = 'TW')

  elif data == 'as' or data == 'lp' or data =='ck':
    topwear = Product.objects.filter(category='TW').filter(brand=data)
    
  elif data == 'below':
    topwear = Product.objects.filter(category='TW').filter(discounted_price__lte=1000)
    print(topwear)

  elif data == 'above':
    topwear = Product.objects.filter(category='TW').filter(discounted_price__gte=1000)
    print(topwear)


  return render(request ,template_name='app/topwear.html', context={'topwear': topwear})


def bottomwear(request, data=None):
  print(data)
  if data==None:
    bottomwear = Product.objects.filter(category = 'BW')

  elif data == 'as' or data == 'lp' or data =='ck' or data=='spy':
    bottomwear = Product.objects.filter(category='BW').filter(brand=data)
    
  elif data == 'below':
    bottomwear = Product.objects.filter(category='BW').filter(discounted_price__lte=2000)
    print(bottomwear)

  elif data == 'above':
    bottomwear = Product.objects.filter(category='BW').filter(discounted_price__gte=3000)
    print(bottomwear)


  return render(request ,template_name='app/bottomwear.html', context={'bottomwear': bottomwear})


class CustomerRegistrationView(View):
  def get(self, request):
    form = CustomerRegistrationForm()
    return render(request, template_name='app/customerregistration.html', context={'form':form})

  def post(self, request):
    form =CustomerRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Congratulations, registered succesfully')
    return render(request, template_name='app/customerregistration.html', context={'form': form}) 




def checkout(request):
 return render(request, 'app/checkout.html')
