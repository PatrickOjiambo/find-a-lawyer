# type: ignore
"""
This module includes functions for creating lawyer,
finding lawyer based on some params and updating lawyer data
"""
from .models import Lawyer
from .serializers import LawyerSerializer
from django.core.exceptions import ObjectDoesNotExist
from typing import Dict, Any


class DB:
    """
    class to perform basic operations on the lawye class
    """

    def add_user(self, user_data: Dict[str, Any]) -> Lawyer:
        """
        function to add a new user
        """
        serializer = LawyerSerializer(data=user_data)
        if serializer.is_valid():
            lawyer = serializer.save()
            return lawyer
        else:
            raise ValueError(serializer.errors)

    def find_user_by(self, **kwargs) -> Lawyer:
        """
        function to find user by some params
        """
        try:
            return Lawyer.objects.get(**kwargs)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist("Lawyer not found")

    def update_user(self, lawyer_id: int, user_data: Dict[str, Any]) -> Lawyer:
        """
        function to update user data
        """
        lawyer = self.find_user_by(lawyer_id=lawyer_id)
        # When instance is passed to the serializer, it updates the instance
        # When no instance is passed, it creates a new instance
        serializer = LawyerSerializer(lawyer, data=user_data, partial=True)
        if serializer.is_valid():
            lawyer = serializer.save()
            return lawyer
        else:
            raise ValueError(serializer.errors)
