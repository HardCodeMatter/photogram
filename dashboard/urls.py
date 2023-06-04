from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard_view, name='d/dashboard'),
    path('accounts/', views.account_list_view, name='d/account_list'),
    path('accounts/<int:id>/posts/', views.account_posts_view, name='d/account_posts'),
]
