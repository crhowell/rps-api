from django.shortcuts import render
from django.db.models import Count, F, Func, Q, Subquery
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers
from . import models
from .utils import attach_game_data, check_player_won


@api_view(['GET', 'POST'])
def all_games(request):
    """
    Generate and return metrics about all games that have taken place.
    """
    if request.method == 'POST':
        # Just a utility helper function to keep the view slimmer looking.
        request = attach_game_data(request)
        serializer = serializers.GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # GET requests
    games = models.GameRound.objects.all_game_stats()
    return Response(games)

