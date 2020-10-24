from django.contrib import admin
from django.urls import path
from foods import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name="home"),
    path('order/<int:pk>', views.HomeDetailView.as_view(), name="order"),
    path('create', views.FoodCreateView.as_view(), name="create"),
    path('edit/<int:pk>', views.FoodEditView.as_view(), name="edit"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('login', views.MyProjectLoginView.as_view(), name="login"),
    path('register', views.RegisterUserView.as_view(), name="register"),
    path('logout', views.MyProjectLogout.as_view(), name="logout"),
]