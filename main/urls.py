from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index" ),
    path('', views.signin, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.sign_out, name='logout'),
    path('userslist', views.userslist, name="userslist"),
    path('users/add/', views.add_user, name='add_user'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),

    # ITEM
    path('items/', views.item_list, name='item_list'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),

    #  CATEGORY
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),

    #     ORDERS
    path('orders/', views.manage_orders, name='orders'),
    path('orders/add/', views.add_order, name='add_order'),
    path('orders/edit/<int:order_id>/', views.edit_order, name='edit_order'),
    path('orders/delete/<int:order_id>/', views.delete_order, name='delete_order'),

    path('order status/<int:id>/', views.order_status, name='order_status'),
    path('sales/', views.sales_overview, name='sales'),
    path('invoices/', views.invoice_list, name='invoices'),
    path('invoices/<int:id>/', views.invoice_detail, name='invoice_detail'),
    path('payments/', views.payment_list, name='payments'),
    path('settings', views.settings, name='settings',),
   
]