from rest_framework import serializers
from .models import User,Role,Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','role', 'account', 'created_at']
        extra_kewargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        role=validated_data.get('role', None),
        user.save()
        return user


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role_name']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account   
        fields = '__all__'


