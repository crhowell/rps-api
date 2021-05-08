from django.utils import timezone
from .serializers import UserSerializer


def my_jwt_response_handler(token, user=None, request=None):
    user = UserSerializer(user, context={'request': request}).data
    now = timezone.now()
    print(now)
    return {
        'token': token,
        'user': user['username'],
        'orig_iat': timezone.now()
    }
