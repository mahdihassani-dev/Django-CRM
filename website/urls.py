from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.home, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:pk>', views.customer_record, name='customer'),
    path('delete/<int:pk>', views.delete_customer, name='delete-customer'),
    path('add-customer/', views.add_record, name='add-customer'),
    path('update/<int:pk>', views.update_customer, name='update-customer'),

]