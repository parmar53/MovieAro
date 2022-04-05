from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.db import models
from .models import movie_type, movie_language, movie_rating_type, Client, movie, m_rating, OrderItem, cart, User, Customer




# Register your models here.

admin.site.register(movie_language)
admin.site.register(movie_rating_type)
admin.site.register(m_rating)

@admin.register(movie_type)
class MovieModek(admin.ModelAdmin):
    list_display = ['id', 't_name']
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','cus_user','c_name','c_locality','c_contact']

@admin.register(movie)
class MovieModelAdmin(admin.ModelAdmin):
    list_display = ['m_name', 'movie_ge', 'm_o_lan', 'm_writer','m_price','m_type']

@admin.register(OrderItem)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'client', 'movie', 'quantity','order_status','order_date']

@admin.register(cart)
class cartModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'o_movie', 'o_quantity']






