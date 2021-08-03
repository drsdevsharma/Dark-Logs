from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('addblog/', views.PostBlog, name = 'addblog'),
    path('update/<int:id>/', views.UpdateBlog, name = 'updateblog'),
    path('delete/<int:id>/', views.DeleteBlog, name = 'delete'),
    
    

    ]