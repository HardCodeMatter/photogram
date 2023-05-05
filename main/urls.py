from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_view, name='post_list'),
    path('post/<int:id>/', views.post_detail_view, name='post_detail'),
    path('post/<int:id>/update/', views.post_update_view, name='post_update'),
    path('post/<int:id>/delete/', views.post_delete_view, name='post_delete'),

    path('post/<int:id>/like/', views.like_add_view, name='like_add'),
]
