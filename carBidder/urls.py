"""carBidder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from carBidderApp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('add_funds/', views.add_funds, name='add_funds'),
    path('report/', views.report, name='report'),
    path('users/', views.users, name='users'),
    path('verify_vehicles/', views.verify_vehicles, name='verify_vehicles'),
    path('chat_with_buyer/', views.chat_with_buyer, name='chat_with_buyer'),
    path('orders/', views.orders, name='orders'),
    path('profile/<int:other_user_id>/',
         views.other_user_profile, name='other_user_profile'),
    path('weekly_reports/', views.weekly_reports, name='weekly_reports'),

    # rating
    path('buyer_rate_seller/<int:order_id>/', views.buyer_rate_seller, name='buyer_rate_seller'),
    path('seller_rate_buyer/<int:listing_id>/', views.seller_rate_buyer, name='seller_rate_buyer'),


    path('search', views.search_car, name="search_car"),
    path('product/<int:listing_id>/', views.product_detail, name='product_detail'),
    path('product/<int:listing_id>/bid', views.bid, name='bid'),
    path('chatbot', views.chatbot, name='chatbot'),
    path('chat/', views.chat, name='chat'),

    path('sell_post', views.sell_post, name='sell_post'),
    path('sell_post_success', views.sell_post_success, name='sell_post_success'),

    path('choose_bid/<int:listing_id>/', views.choose_bid, name='choose_bid'),
    path('execute-query/', views.execute_query, name='execute_query'),
]
