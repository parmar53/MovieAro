"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .form import mypasswordchangeform

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.movieview.as_view(), name='home'),
    path('signup/', views.CustomerRegistrationView.as_view(), name='signup'),
    path('login', views.log_in, name='log_in'),
    path('movie_list1/<slug:dba>', views.movie_list1, name='movie_list'),
    path('movie_list/<slug:db>', views.movie_list, name='movie_list1'),
    path('bollywood/<slug:data>', views.movie_filter, name='movie_filter'),
    # path('reset_password/', views.reset, name='reset'),
    # path('top', views.top, name='top'),
    path('base', views.base, name='base'),
    path('address',views.address, name='address'),
    path('logout/', views.user_logout, name='user_logout'),
    path('mycart/', views.mycart, name='mycart'),
    path('cart/', views.show_cart, name='cart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.paymentdone, name='paymentdone'),
    path('removecart/', views.removecart, name='removecart'),
    path('orders/', views.orders, name='orders'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='myapp1/passwordchangedone.html') ,name='passwordchangedone'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name= 'myapp1/passwordchange.html', form_class=mypasswordchangeform, success_url='/passwordchangedone/'), name='changepassword'),
    #path('logout/', auth_view.LogoutView.as_view(), name='user_logout'),
    path('profile/', views.user_profile.as_view(), name='user_profile'),
    path('movie_detail/<int:pk>', views.movie_detail_view.as_view(), name='movie_d'),

    #path('logout', views.logout, name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

