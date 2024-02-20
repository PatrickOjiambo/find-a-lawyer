#type: ignore
"""
This file contains the views for the authentication_service app.
"""
from .models import Lawyer
from .serializers import LawyerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class  LawyerList(APIView):
    """
    Create an account as a lawyer.
    """
    def post(self, request, format=None):
        """
        Create a new lawyer account.
        """
        
    