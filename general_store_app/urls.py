from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path('products/<str:category>/', views.category_products, name="category_products"),
    path('contact/', views.contact, name='contact'),
]
