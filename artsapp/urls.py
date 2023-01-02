from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('aboutme/', views.about, name='about'),
    path('contactme/', views.contact, name='contact'),
    path('art/<int:pk>', views.details, name='art_details'),
    path('signinpage/', views.openSignIn, name='opensignin'),
    path('signuppage/', views.openSignUp, name='opensignup'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout/', views.signout, name='signout')
]
