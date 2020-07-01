"""codingunda URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import index, about, post, \
    contact, search, view_all,product_settings,\
    product_and_stock,support_and_feedback,online_and_store

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('post/<int:id>/<slug:slug>', post, name='post'),
    path('contact/', contact, name='contact'),
    path('search/', search, name='search'),
    path('view_all/<str:query>', view_all, name='view_all'),
    path('ckeditor/', include('ckeditor_uploader.urls')),





    path('support_and_feedback/', support_and_feedback, name='support_and_feedback'),
    path('online_and_store/', online_and_store, name='online_and_store'),

    path('product_and_stock/', product_and_stock, name='product_and_stock'),

    path('product_settings/', product_settings, name='product_settings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
