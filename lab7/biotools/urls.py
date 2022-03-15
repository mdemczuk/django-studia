from django.urls import path

from . import views

app_name = 'biotools'

urlpatterns = [
    path('seqcontent/', views.seqcontent_view, name='seqcontent'),
]