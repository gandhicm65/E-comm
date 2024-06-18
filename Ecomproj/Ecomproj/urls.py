"""
URL configuration for Ecomproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Ecomapp import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('register/',views.register, name="register"),
    path('login/',views.login_page, name="login_page"),
    path('logout/',views.logout_page, name="logout_page"),
    path('cart/',views.cart_page, name="cart_page"),
    path('cart_remove/<cid>',views.cart_remove, name="cart_remove"),
    path('fav_remove/<fid>',views.fav_remove, name="fav_remove"),
    path('fav/',views.fav_page, name="fav"),
    path('fav_view_page/',views.fav_view_page, name="fav_view_page"),
    path('collections/',views.collections, name='collect'),
    path('collections/<name>',views.collectionsview, name='collectview'),
    path('collections/<cname>/<pname>',views.product_details, name='product_details'),
    path('addtocart/',views.add_to_cart, name="addtocart"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)