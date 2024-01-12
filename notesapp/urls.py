from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.list),
    path('notes/<int:pk>/', views.detail),
    # path('add/', views.add),
    # path('edit/<int:id>/', views.edit),
    # path('delete/<int:id>/', views.delete),
]