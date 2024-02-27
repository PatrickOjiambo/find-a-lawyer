# type: ignore
"""
This file contains the views for the authentication_service app.
"""
from .models import Lawyer
from .serializers import LawyerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .auth_utils import jwt_authentication, decode_token
import datetime
from jwt.utils import get_int_from_datetime
from rest_framework.decorators import api_view
from .complete_profile import CompleteProfile
from .auth_utils import LawyerAuth
LAWYERAUTH = LawyerAuth()
COMPLETEPROFILE = CompleteProfile()


@api_view(['POST'])
def register_lawyer(request):
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


@api_view(['POST'])
def login(request):
    """
    Login as a lawyer endpoint
    """
    login_data = request.data
    try:
        is_logged_in = LAWYERAUTH.validate_login(login_data)
        if is_logged_in:
            jwt_user_info = {
                "email": request.data["email"],
                # Token expiration time
                "exp": get_int_from_datetime(datetime.datetime.utcnow() + datetime.timedelta(hours=3))
            }
            token = jwt_authentication(jwt_user_info)
            return Response({"token": token}, status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid password"}, status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def complete_profile(request):
    """
    Complete profile endpoint
    """
    user_data = request.data
    token = decode_token(request.headers['jwt-auth'])
    try:
        COMPLETEPROFILE.complete_profile(token["email"], user_data)
        return Response({"message": "Profile updates successfully"}, status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
