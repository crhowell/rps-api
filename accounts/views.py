from django.db.models import Count, Q
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers


User = get_user_model()


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    games = request.user.game_rounds.aggregate(
        total_wins=Count('pk', filter=Q(player_has_won=True)),
        total_losses=Count('pk', filter=Q(player_has_won=False)),
        total_ties=Count('pk', filter=Q(player_has_won=None)),
        total_games=Count('pk')
    )
    serializer = serializers.UserSerializer(request.user)
    games.update(serializer.data)
    return Response(games)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    serializer = serializers.UserSerializerWithToken(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_profile(request):
    """
    Generate and return game metrics about the current user.
    """
    # request.user should be a User model,
    # I can use reverse relation to games.
    # AKA creator = models.ForeignKey(User, related_name='game_rounds',
    games = request.user.game_rounds.aggregate(
        total_wins=Count('pk', filter=Q(player_has_won=True)),
        total_losses=Count('pk', filter=Q(player_has_won=False)),
        total_ties=Count('pk', filter=Q(player_has_won=None)),
        total_games=Count('pk')
    )
    return Response(games)