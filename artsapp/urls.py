from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('aboutme/', views.about, name='about'),
    path('contactme/', views.contact, name='contact'),
    path('art/<int:pk>', views.details, name='art_details'),
]
