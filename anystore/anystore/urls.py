"""anystore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from mainapp import views as mainapp_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp_views.main, name='main'),
    path('products/', mainapp_views.products, name='products'),
    path('contact', mainapp_views.contact, name='contact'),

    path('products/all/', mainapp_views.products, name='products_all'),
    path('products/home/', mainapp_views.products, name='products_home'),
    path('products/office/', mainapp_views.products, name='products_office'),
    path('products/modern/', mainapp_views.products, name='products_modern'),
    path('products/classic/', mainapp_views.products, name='products_classic'),

]


