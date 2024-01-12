from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name='notes.list'),
    path('notes/<int:pk>/', views.NotesDetailView.as_view(), name='notes.description'),
    # path('add/', views.add),
    # path('edit/<int:id>/', views.edit),
    # path('delete/<int:id>/', views.delete),
]