from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Child
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)  # Asegúrate de que el email sea validado correctamente
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


    def validate_username(self, value):
        """
        Validación personalizada para verificar si el nombre de usuario ya existe.
        """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate_email(self, value):
        """
        Validación personalizada para verificar si el email ya existe.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("An account with this email already exists.")
        return value

    def create(self, validated_data):
        """
        Crear el usuario después de validar que el username y email sean únicos.
        """
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['id', 'first_name', 'date_of_birth']


class UserDetailSerializer(serializers.ModelSerializer):
    children = ChildSerializer(many=True)  # Añadir los hijos del usuario

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'children']


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, data):
        # Solo validar si el usuario está cambiando la contraseña
        if 'password' in data:
            if 'confirm_password' not in data:
                raise serializers.ValidationError({"confirm_password": "You must confirm the new password."})
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError({"password": "Passwords must match."})
        return data

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        # Solo actualizar la contraseña si se proporciona
        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance


