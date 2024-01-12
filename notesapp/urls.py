from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view()),
    path('notes/<int:pk>/', views.NotesDetailView.as_view()),
    # path('add/', views.add),
    # path('edit/<int:id>/', views.edit),
    # path('delete/<int:id>/', views.delete),
]