from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('postdetail/<slug:slug>/<int:pk>/', views.postdetail, name='post_detail'),
    path('postlist/<slug:tag_slug>/', views.postlist, name="post_list_tag"),
    path('postlist/', views.postlist, name="post_list"),
    path('account-form/', views.useraccount, name="user-account"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.register, name="register"),
    path('category/<slug:category_slug>/', views.postlist, name='post_list_by_category'),
    path('change-password/', views.change_password, name="change-password"),
    path('contact-us/', views.contactus, name="contact-us"),
    path('search/', views.search, name="search"),
]
