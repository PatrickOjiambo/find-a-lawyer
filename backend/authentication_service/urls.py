#type: ignore
from django.urls import path
from .lawyerView import LawyerList
urlpatterns = [
path('auth/lawyer-sign-up', LawyerList.as_view(), name="lawyer-sign-up")
]