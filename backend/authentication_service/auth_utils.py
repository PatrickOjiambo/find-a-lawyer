# type: ignore
"""
utils for the authentication service app
"""
import bcrypt
import os
from jwt import JWT, jwk_from_dict
from .models import Lawyer
from .serializers import LawyerSerializer
instance = JWT()


def hash_password(password):
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
    def create_lawyer():
        """
        Function that creates a lawyer in the database
        """
        pass
    