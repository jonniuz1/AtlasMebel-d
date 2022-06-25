from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    path('service/', views.service, name='service'),
    path('single/', views.single, name='single'),
]