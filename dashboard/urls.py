from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('allauth.urls')),
    path('', views.main , name='main'),
    path('login/dashboard/',TemplateView.as_view(template_name='board/index.html'))
]
