# type: ignore
"""
This file contains the views for the authentication_service app.
"""
from .models import Lawyer
from .serializers import LawyerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .auth_utils import jwt_authentication
import datetime
from jwt.utils import get_int_from_datetime
from .auth_utils import LawyerAuth
LAWYERAUTH = LawyerAuth()


class LawyerList(APIView):
    """
    Create an account as a lawyer.
    """

    def post(self, request, format=None):
        """
        Create a new lawyer account. This function is for signing up.
        """
        signup_info = request.data

        jwt_user_info = {
            "email": request.data["email"],
            # Token expiration time
            "exp": get_int_from_datetime(datetime.datetime.utcnow() + datetime.timedelta(hours=3))
        }
        try:
            LAWYERAUTH.register_lawyer(signup_info)
            token = jwt_authentication(jwt_user_info)
            return Response({"token": token}, status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
