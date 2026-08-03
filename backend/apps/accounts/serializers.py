import re
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'phone', 'role',
            'first_name', 'last_name', 'full_name',
            'is_active', 'is_frozen', 'last_login',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'last_login', 'created_at', 'updated_at']
        
    def get_full_name(self, obj):
        return obj.full_name 
        
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password', 'password2', 'first_name', 'last_name', 'role']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def validate_email(self, value):
        try:
            validate_email(value)
        except:
            raise serializers.ValidationError("Invalid email format.")
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    
    def validate_phone(self, value):
        # Clean and validate BD Phone number
        phone_number = re.sub(r'\D', '', value)
        if phone_number.startswith('88'):
            phone_number = phone_number[2:]
            
        if len(phone_number) != 11 or not phone_number.startswith('01'):
            raise serializers.ValidationError("Invalid phone number. Must be 11 digits and start with 01.")
        
        if User.objects.filter(phone=phone_number).exists():
            raise serializers.ValidationError("A user with this phone number already exists.")
        return phone_number
    
    def validate_role(self, value):
        allowed_roles = ['Vendor', 'Junior Manager']
        if value not in allowed_roles:
            raise serializers.ValidationError(
                f"Role must be one of: {', '.join(allowed_roles)}"
            )
        return value
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):  # Changed to Serializer from ModelSerializer
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
      
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("No user found with this email.")
        
        if not user.is_active:  
            raise serializers.ValidationError("This account is inactive.")
        
        if user.is_frozen:
            raise serializers.ValidationError("This account is frozen. Please contact support.")
        
        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid password.")
        
        attrs['user'] = user
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])  # Fixed 'validators' syntax
    confirm_new_password = serializers.CharField(required=True)
    
    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_new_password']:
            raise serializers.ValidationError({"confirm_new_password": "New passwords didn't match."})  # Fixed dict structure
        return attrs


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone']
        
    def validate_phone(self, value):
        phone_number = re.sub(r'\D', '', value)
        if phone_number.startswith('88'):
            phone_number = phone_number[2:]
            
        if len(phone_number) != 11 or not phone_number.startswith('01'):
            raise serializers.ValidationError("Invalid phone number. Must be 11 digits and start with 01.")
        
        user_qs = User.objects.filter(phone=phone_number)
        if self.instance and self.instance.id:
            user_qs = user_qs.exclude(id=self.instance.id)            
        if user_qs.exists():
            raise serializers.ValidationError("This phone number is already in use.")
        return phone_number
    

class UserListSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'phone', 'role',
            'first_name', 'last_name', 'full_name',
            'is_active', 'is_frozen'
        ]
    
    def get_full_name(self, obj):
        return obj.full_name


class UserDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'phone', 'role',
            'first_name', 'last_name', 'full_name',
            'is_active', 'is_frozen', 'last_login',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'last_login', 'created_at', 'updated_at']
    
    def get_full_name(self, obj):
        return obj.full_name


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'phone', 'password', 'password2',
            'first_name', 'last_name', 'role', 'is_active'
        ]
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    
    def validate_phone(self, value):
        phone_number = re.sub(r'\D', '', value)
        if phone_number.startswith('88'):
            phone_number = phone_number[2:]

        if len(phone_number) != 11 or not phone_number.startswith('01'):
            raise serializers.ValidationError("Invalid phone number. Must be 11 digits and start with 01.")

        if User.objects.filter(phone=phone_number).exists():
            raise serializers.ValidationError("A user with this phone number already exists.")
        return phone_number
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
