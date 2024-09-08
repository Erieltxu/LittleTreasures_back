from django.urls import path, include
from .views import RegisterView, UserLoginView, LogoutView, UserDetailView, UserUpdateView, UserDeleteView
from rest_framework.routers import DefaultRouter
from .views import ChildViewSet

# Crear el router e incluir el ViewSet de Child
router = DefaultRouter()
router.register(r'children', ChildViewSet, basename='child')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserDetailView.as_view(), name='profile'),  # Vista de perfil
    path('profile/update/', UserUpdateView.as_view(), name='profile-update'),  # Actualizar perfil
    path('profile/delete/', UserDeleteView.as_view(), name='profile-delete'),  # Eliminar cuenta
    path('', include(router.urls)),
]
