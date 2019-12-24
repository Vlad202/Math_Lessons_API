from authApp.models import UserToken
from rest_framework.response import Response

def is_staff_only(token):
    try:
        user = UserToken.objects.get(token=token).user.is_staff 
        if user:
            return True
        else:
            return False
    except: 
        return False