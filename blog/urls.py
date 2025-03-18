from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('blog/posts/', views.posts, name='posts'),
    # Create Post page
    path('create/', views.create_post, name='create_post'),
    # Detail page
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    # Upadte page
    path('post/<int:pk>/edit/', views.post_update, name='post_update'),
    # Delete Button
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]

