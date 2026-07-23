from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    full_name=serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'phone', 'role',
            'first_name', 'last_name', 'full_name',
            'is_active', 'is_frozen', 'last_login',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'last_login', 'created_at', 'updated_at']
        def get_full_name(self,obj):
            return obj.full_name 