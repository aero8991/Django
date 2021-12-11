from django.urls import path
from . import views

urlpatterns = [
    path('home.html', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('blog.html', views.blog, name='blog'),
    path('detail.html', views.detail, name='detail'),
    path('service.html', views.service, name='service'),
    path('team.html', views.team, name='team'),
    path('testimonial.html', views.testimonial, name='testimonial'),
    path('about.html', views.about, name='about'),
]
