from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('index/', views.index, name='index'),  # URL for index view
    path('postdetail/<slug:slug>/<int:pk>/', views.postdetail, name='post_detail'),
    path('postlist/<slug:tag_slug>/', views.postlist, name="post_list_tag"),
    path('postlist/', views.postlist, name="post_list"),
    path('account-form/', views.useraccount, name="user-account"),
    path('contact-us/', views.contactus, name="contact-us"),
]
