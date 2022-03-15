from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list_view, name="post_list_view"),
]
