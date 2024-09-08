from rest_framework import generics, permissions, views, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserDetailSerializer,
    UserUpdateSerializer,
    ChildSerializer
)
from rest_framework import viewsets
from .models import Child
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Permitir a cualquiera registrarse


class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]  # Permitir a cualquiera intentar loguearse

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user:
                Token.objects.filter(user=user).delete()
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]  # Solo permitir logout si el usuario está autenticado

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"message": "Token not found"}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  # Retornar el usuario autenticado


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  # Retornar el usuario autenticado para actualizar sus datos


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  # Eliminar el usuario autenticado


class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

    def get_queryset(self):
        # Si necesitas que los usuarios solo vean sus propios hijos, puedes filtrar aquí
        user = self.request.user
        return Child.objects.filter(user=user)

    def perform_create(self, serializer):
        # Asociar el hijo creado con el usuario autenticado
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # Puedes realizar acciones adicionales en la actualización si es necesario
        serializer.save()

    def perform_destroy(self, instance):
        # Puedes realizar acciones adicionales al eliminar un hijo si es necesario
        instance.delete()