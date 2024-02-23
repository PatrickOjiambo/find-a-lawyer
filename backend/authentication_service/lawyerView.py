# type: ignore
"""
This file contains the views for the authentication_service app.
"""
from .models import Lawyer
from .serializers import LawyerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .auth_utils import hash_password, jwt_authentication
import datetime
from jwt.utils import get_int_from_datetime


class LawyerList(APIView):
    """
    Create an account as a lawyer.
    """

    def post(self, request, format=None):
        """
        Create a new lawyer account. This function is for signing up.
        """
        signup_info = request.data
        password = signup_info["password_hash"]
        password_hash = hash_password(password)
        jwt_user_info = {
            "email": request.data["email"],
            # Token expiration time
            "exp": get_int_from_datetime(datetime.datetime.utcnow() + datetime.timedelta(hours=3))
        }
        signup_info["password_hash"] = password_hash
        serializer = LawyerSerializer(data=signup_info)
        if serializer.is_valid():
            lawyer = serializer.save()
            jwt_user_info["id"] = lawyer.lawyer_id
            token = jwt_authentication(jwt_user_info)
            print(token)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
