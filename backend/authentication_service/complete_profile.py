# type: ignore
"""
Controller file for completing lawyer profile
"""
from .models import Lawyer
from .db import DB
import os
from dotenv import load_dotenv
import boto3
from typing import Dict, Any
import uuid
load_dotenv()


def upload_image_s3(file_path) -> str:
    """
    Upload image to s3 bucket
    """

    s3 = boto3.client('s3', aws_access_key_id=os.getenv('ACCESSKEY'),
                      aws_secret_access_key=os.getenv('SECRETACCESSKEY'))
    key = f"images/{uuid.uuid4()}.jpg"
    s3.upload_fileobj(file_path, os.getenv('BUCKETNAME'), key)
    return f"https://{os.getenv('BUCKETNAME')}.s3.us-east-1.amazonaws.com/{key}"


def upload_file_s3(file_path) -> str:
    """
    Upload file to s3 bucket
    """

    s3 = boto3.client('s3', aws_access_key_id=os.getenv('ACCESSKEY'),
                      aws_secret_access_key=os.getenv('SECRETACCESSKEY'))
    key = f"files/{uuid.uuid4()}.pdf"
    s3.upload_fileobj(file_path, os.getenv('BUCKETNAME'), key)
    return f"https://{os.getenv('BUCKETNAME')}.s3.amazonaws.com/{key}"


class CompleteProfile:
    """
    Class contains functions to complete the user profile
    """

    def __init__(self):
        self._db = DB()

    def complete_profile(self,email: str, user_data: Dict[str, Any]):
        """
        function contains user details for updating
        lawyer profile || completing profile.
        """

        lawyer = self._db.find_user_by(email=email)
        if not lawyer:
            raise Exception("User not found")
        try:
            if 'image_file' in user_data:
                image_url = upload_image_s3(user_data['image_file'])
                del user_data['image_file']
                user_data['image_url'] = image_url
            if 'resume_file' in user_data:
                lawyer_resume = upload_file_s3(user_data['resume_file'])
                del user_data['resume_file']
                user_data['lawyer_resume'] = lawyer_resume
            lawyer = self._db.update_user(lawyer.lawyer_id, user_data)
        except Exception as e:
            raise e
        return lawyer
