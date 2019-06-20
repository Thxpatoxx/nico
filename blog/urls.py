from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('Diagnostico/<int:pk>/', views.post_detail, name='post_detail'),
    path('Diagnostico/new', views.post_new, name='post_new'),
    path('Diagnostico/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('accounts/', include('django.contrib.auth.urls')),
]