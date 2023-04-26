from django.shortcuts import render, redirect
from .models import Product, Customer, Order_Placed, Cart
from django.views import View
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse 
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
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Cart(user=user, product=product).save()
 return redirect('/cart')

def show_cart(request):
  if request.user.is_authenticated:
    user =request.user
    cart = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_products = [p for p in Cart.objects.all() if p.user == request.user]
    
    if cart_products:
      for p in cart_products:
        tempamount = (p.quantity * p.product.discounted_price)
        amount+=tempamount
        total_amount = amount+shipping_amount
      return render(request, template_name='app/addtocart.html', 
            context={'carts': cart, 'amount':amount, 'totalamount':total_amount})
    return render(request, template_name='app/emptycart.html')


def plus_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity+=1
    c.save()
    amount =0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]

    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount+=tempamount

    data ={
    'quantity': c.quantity,
    'amount': amount,
    'totalamount':amount +shipping_amount
    }

    return JsonResponse(data)



def minus_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity-=1
    c.save()
    amount =0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]

    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount+=tempamount

    data ={
    'quantity': c.quantity,
    'amount': amount,
    'totalamount':amount+shipping_amount
    }

    return JsonResponse(data)

def remove_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.delete()
    amount =0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]

    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount+=tempamount
     

    data ={
    'amount': amount,
    'totalamount':amount + shipping_amount
    }

    return JsonResponse(data)
  

def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

class ProfileView(View):
  def get(self, request):
    form = CustomerProfileForm()
    return render(request, template_name='app/profile.html', context={'form': form})
  
  def post(self, request):
    form = CustomerProfileForm(request.POST)
    if form.is_valid():
      usr = request.user
      print(usr)
      name = form.cleaned_data['name']
      locality = form.cleaned_data['locality']
      city = form.cleaned_data['city']
      zipcode = form.cleaned_data['zipcode']
      state = form.cleaned_data['state']

      reg = Customer(user=usr, name=name, locality=locality, city=city, zipcode=zipcode, state=state)
      reg.save()
      messages.success(request, "Added Succesfully")
    return render(request, template_name='app/profile.html', context={'form':form})


# def address(request):
#  return render(request, 'app/address.html')

class AddressView(View):
  
  def get(self, request):
    add = Customer.objects.filter(user= request.user)
    return render(request, template_name='app/address.html', context={'add': add})

def orders(request):
 op= Order_Placed.objects.filter(user=request.user)
 print(op)
 return render(request, 'app/orders.html', context={'order_placed':op})

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
 user = request.user
 add = Customer.objects.filter(user=user)  
 cart_items = Cart.objects.filter(user=user)

 amount =0.0
 shipping_amount = 70.0
 cart_product = [p for p in Cart.objects.all() if p.user == request.user]
 
 if cart_product:
  for p in cart_product:
    tempamount = (p.quantity * p.product.discounted_price)
    amount+=tempamount
 totalamount = amount+shipping_amount
 print(add)
 return render(request, 'app/checkout.html', context = {'add':add,
                                       'totalamount':totalamount, 'cart_items':cart_items} )

def payment_done(request):
  user = request.user
  custid = request.GET.get('custid')
  print(custid)
  customer =Customer.objects.get(id=custid)
  cart = Cart.objects.filter(user=user)
  for c in cart:
    Order_Placed(user=user, customer=customer, product=c.product, quantity =c.quantity).save()
    c.delete()
  return redirect('orders')