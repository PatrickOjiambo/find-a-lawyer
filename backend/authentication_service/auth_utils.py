# type: ignore
"""
utils for the authentication service app
"""
import bcrypt
from typing import Dict, Any
from jwt import JWT, jwk_from_dict
from .models import Lawyer
from .serializers import LawyerSerializer
from .db import DB
instance = JWT()


def _hash_password(password):
    """
    given a password, generate a hash of the password
    """
    pass_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(pass_bytes, salt)
    return password_hash.decode('utf-8')


def jwt_authentication(user_info):
    """
    given user info, generate a jwt token
    """
    # Key for testing purposes
    signing_key = jwk_from_dict({'kty': 'oct', 'k': '...'})
    token = instance.encode(user_info, signing_key, alg="HS256")
    return token


class LawyerAuth:
    """
    This class handles all auth stuff that concerns the lawyer
    """

    def __init__(self):
        self._db = DB()

    def register_lawyer(self, user_data: Dict[str, Any]) -> Lawyer:
        """
        Function that creates a lawyer in the database
        """
        required_fields = ["first_name", "last_name",
                           "email", "password", "phone"]
        if not all(key in user_data for key in required_fields):
            raise ValueError(
                'user_data is missing one or more required fields. check your user_data dict')
        exists = Lawyer.objects.filter(
            email=user_data["email"]).first() is not None
        if exists is True:
            raise ValueError(
                "Lawyer {} already exists".format(user_data["email"]))
        hashed_password = _hash_password(user_data["password"])
        user_data["password_hash"] = hashed_password
        # Delete the old password from the dictionary
        del user_data["password"]
        return self._db.add_user(user_data)
