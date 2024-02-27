#type: ignore
from django.urls import path
from .lawyerView import register_lawyer, login, complete_profile
urlpatterns = [
path('auth/lawyer-sign-up', register_lawyer, name="lawyer-sign-up"),
path('auth/lawyer-login', login, name="lawyer-login"),
path('auth/lawyer-complete-profile', complete_profile, name="complete-profile")
]