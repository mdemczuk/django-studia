from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list_view, name='post_list_view'),
    path('post/<int:post_id>/', views.post_detail_view, name="post_detail_view"),
    path('author/<int:author_id>/', views.post_list_view, name="post_list_author"), 
    path('category/<category_name>/', views.post_list_view, name="post_list_category"),
]
