"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import c_home
from contact_manager.views import c_form, c_form_edit, c_form_delete, c_forms_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', c_home, name='c_home'),
    path('contact_form', c_form, name='c_form'),
    path('country_form', c_forms_form, name='c_forms_form'),
    path('contact_form/edit/<int:contact_id>', c_form_edit, name='c_form_edit'),
    path('contact_form/delete/<int:contact_id>', c_form_delete, name='c_form_delete'),
]
