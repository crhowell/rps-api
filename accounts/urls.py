from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

# path('user', include(('accounts.urls', 'accounts'))),
# ^ 'user' is the prefix for all these sub-routes. 
urlpatterns = [
    # POST -> login route.
    path('user/token', obtain_jwt_token, name='login'),
    path('user/refresh-token', refresh_jwt_token),
    path('user/verify-token', verify_jwt_token),
    # GET -> Retrieve my current user.
    path('user/profile', views.current_user, name='current-user'),
    # POST -> Register new user.
    path('user', views.create_user, name='create-user')
]