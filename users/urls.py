from django.urls import path
from .views import RegisterView, UserLoginView, LogoutView, UserDetailView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserDetailView.as_view(), name='profile'),  # Vista de perfil
    path('profile/update/', UserUpdateView.as_view(), name='profile-update'),  # Actualizar perfil
    path('profile/delete/', UserDeleteView.as_view(), name='profile-delete'),  # Eliminar cuenta
]
