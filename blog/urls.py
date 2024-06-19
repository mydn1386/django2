from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('index/', views.index, name='index'),  # URL for index view
    path('postdetail/<slug:post>/<int:pk>', views.postdetail, name='post_detail'),  # URL for post detail view
    path('postlist/', views.postlist, name="post_list"),
    path('account-form/', views.useraccount, name="user-account"),
    # path('postlist/', views.PostListView.as_view(), name='post_list'),  # URL for post list view
]