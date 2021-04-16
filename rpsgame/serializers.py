from rest_framework import serializers

from . import models


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GameRound
        fields = [
            'player_choice',
            'creator',
            'bot',
            'bot_choice',
            'player_has_won'
        ]
        read_only_fields = ['created_at']