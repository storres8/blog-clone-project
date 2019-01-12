from django.urls import path, include
from blog import views


app_name = 'blog'

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_view'),
    path('post/<slug:pk>/edit', views.PostUpdateView.as_view(), name='post_update'),
    path('drafts/'views.DraftListView.as_view(), name='post_draft_list'),
]
