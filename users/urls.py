from django.urls import path
from .views import (RegisterView, UserLoginView, LogoutView, UserDetailView, UserUpdateView, UserDeleteView,
                    ChildViewSet, RegisterChildView)
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'children', ChildViewSet, basename='child')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('profile/update/', UserUpdateView.as_view(), name='profile-update'),
    path('profile/delete/', UserDeleteView.as_view(), name='profile-delete'),
    path('registrations/', RegisterChildView.as_view(), name='register-child'),
]+ router.urls
