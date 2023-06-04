from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_view, name='post_list'),
    path('post/<int:id>/', views.post_detail_view, name='post_detail'),
    path('post/create/', views.post_create_view, name='post_create'),
    path('post/<int:id>/update/', views.post_update_view, name='post_update'),
    path('post/<int:id>/delete/', views.post_delete_view, name='post_delete'),

    path('comment/<int:id>/update/', views.comment_update_view, name='comment_update'),
    path('comment/<int:id>/delete/', views.comment_delete_view, name='comment_delete'),

    path('post/<int:id>/like/', views.like_add_view, name='like_add'),

    path('post/<int:id>/report/', views.report_create_view, name='report_create'),
    path('post/<int:id>/status/', views.post_status_view, name='post_status')
]
