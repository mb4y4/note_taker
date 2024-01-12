from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('authorized/', views.AuthorizedViews.as_view()),
]