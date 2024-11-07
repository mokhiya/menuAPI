from django.urls import path
from .views import MenuViewSet, CommentViewSet

app_name = 'menu'

urlpatterns = [
    path('menu/', MenuViewSet.as_view({'get': 'list', 'post': 'create'}), name='menu-list'),
    path('menu/<int:pk>/', MenuViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='menu-detail'),

    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='comment-detail'),
]