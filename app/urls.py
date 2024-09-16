from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.redirect_to_login, name='redirect_to_login'),
    path('signup/', views.custom_signup, name='custom_signup'),
    path('login/', views.custom_login, name='custom_login'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('upload_data/', views.upload_data, name='upload_data'),
    path('get_users/', views.get_users, name='get_users'),
    path('add_user/', views.add_user, name='add_user'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('query_builder/', views.query_builder, name='query_builder'),
]
