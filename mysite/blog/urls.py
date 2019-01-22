from django.urls import path, include
from blog import views


app_name = 'blog'

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<slug:pk>/edit', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:pk>/remove',views.PostDeleteView.as_view(), name='post_remove')
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<slug:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    path('comments/<slug:pk>/approve', views.comment_approve, name='comment_approve'),
    path('comments/<slug:pk>/remove', views.comment_remove, name='comment_remove'),
    path('post/<slug:pk>/publish',views.post_publish, name='post_publish'),
]
