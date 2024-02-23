#type: ignore
from rest_framework import serializers
from .models import Client, Lawyer, Lawyer_practice_areas, Reviews, Roles
class ClientSerializer(serializers.ModelSerializer):
    """
    Client Serializer"""
    class Meta:
        model = Client
        fields = '__all__'
class LawyerSerializer(serializers.ModelSerializer):
    """
    Lawyer Serializer"""
    class Meta:
        model = Lawyer
        fields = '__all__'
class Lawyer_practice_areasSerializer(serializers.ModelSerializer):
    """
    Lawyer_practice_areas Serializer"""
    class Meta:
        model = Lawyer_practice_areas
        fields = '__all__'
class ReviewsSerializer(serializers.ModelSerializer):
    """
    Reviews Serializer"""
    class Meta:
        model = Reviews
        fields = '__all__'
class RolesSerializer(serializers.ModelSerializer):
    """
    Roles Serializer"""
    class Meta:
        model = Roles
        fields = '__all__'
