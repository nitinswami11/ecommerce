from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductView, ProductDetailView, laptop, topwear, CustomerRegistrationView, ProfileView
from .views import AddressView, show_cart, plus_cart, minus_cart, remove_cart, payment_done
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
urlpatterns = [
    path('', ProductView.as_view(), name='home'),

    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),

    path('cart/', show_cart, name='showcart'),

    path('pluscart/', plus_cart, name='pluscart'),

    path('minuscart/', minus_cart, name='minuscart'),

    path('removecart/', remove_cart, name='removecart'),

    path('checkout/', views.checkout, name='checkout'),

    path('paymentdone/', payment_done, name='paymentdone'),

    path('buy/', views.buy_now, name='buy-now'),

    path('profile/', ProfileView.as_view(), name='profile'),

    path('address/', AddressView.as_view(), name='address'),

    path('orders/', views.orders, name='orders'),

    path('mobile/', views.mobile, name='mobile'),

    path('mobile/<slug:data>/', views.mobile, name='mobiledata'),

    path('laptop/', views.laptop, name='laptop'),

    path('laptop/<slug:data>/', views.laptop, name='laptopdata'),

    path('topwear/', views.topwear, name='topwear'),

    path('topwear/<slug:data>/', views.topwear, name='topwear'),

    path('bottomwear/', views.bottomwear, name='bottomwear'),

    path('bottomwear/<slug:data>/', views.bottomwear, name='bottomwear'),

    path('accounts/login', auth_views.LoginView.as_view(template_name='app/login.html',
                             authentication_form = LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name = 'logout'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(
            template_name = 'app/passwordchange.html', 
            form_class =MyPasswordChangeForm, success_url='/passwordchangedone/'), 
            name='passwordchange'),

    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
            template_name='app/passwordchangedone.html'), 
            name='passwordchangedone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
            template_name='app/password_reset.html', form_class= MyPasswordResetForm), 
            name='password_reset'),
    
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='app/password_reset_done.html'), 
            name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), 
            name='password_reset_confirm'),
    
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
            template_name='app/password_reset_complete.html'), 
            name='password_reset_complete'),

    path('registration/', CustomerRegistrationView.as_view(), name='customerregistration'),

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
