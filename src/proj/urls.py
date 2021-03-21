"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from books import views as bookviews
from dictionaries import urls as dictionaries_urls 
from books import urls as books_urls
from accounts import urls as accounts_urls
from carts import urls as carts_urls
from orders import urls as orders_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bookviews.HomePage.as_view(), name='home-page'),  
    path('dictionaries/', include(dictionaries_urls)),
    path('accounts/', include(accounts_urls)),
    path('book/', include(books_urls)),
    path('cart/', include(carts_urls, namespace='cart')),
    path('order/', include(orders_urls, namespace='order'))   
] 

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
