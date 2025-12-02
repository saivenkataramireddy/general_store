from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path('products/<str:category>/', views.category_products, name="category_products"),
    path('contact/', views.contact, name='contact'),
    path('dashboard/edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('dashboard/delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    # Custom Admin Dashboard
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/add-product/', views.add_product, name='add_product'),
]
