"""
URL configuration for trendwear project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from .import views as v
from .views import checkout, payment_success, payment_cancel


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index),
    path('register',v.register_view),
    path('login',v.login_view),
    path('logout',v.logout_view),
    path('myprofile',v.myprofile,name="myprofile"),
    path('customer_service',v.customer_servivce),
    path('womenlist',v.women_p_list),
    path('menlist',v.men_list),
    path('tops',v.tops_view),
    path('addtocart/<int:pid>',v.add_to_cart),
    path('clist',v.cart_list),
    path('delete1/<int:pk>',v.delete_cart.as_view()),
    path('category/<int:category_id>/', v.products_by_category, name='products_by_category'),
    path('product_search',v.product_search,name='product_search'),
    path('sort',v.gen_list,name='sort'),
    # path('section', v.product_list_view, name='product_list'),
    path('section   /<str:section>/', v.section_view, name='section_view'),
    path('checkout/',v.checkout,name="checkout"),
    path('payment-success/', payment_success, name='payment_success'),
    path('payment-cancel/', payment_cancel, name='payment_cancel'),
    

]
