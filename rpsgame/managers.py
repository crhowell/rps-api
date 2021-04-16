from django.db import models
from django.db.models import Count, Q


class GameRoundManager(models.Manager):
    def all_game_stats(self):
        """Model Managers are for table-wide queries.

        Letting us write in our own custom method like `.objects.all()`.
        Except this one will be `GameRound.objects.all_game_stats()`
        
        This one is doing aggregate total counts across different fields
        using different filters.
        """
        return self.aggregate(
            games_played=Count('pk'),
            unique_plays=Count('creator', distinct=True),
            human_wins=Count('pk', filter=Q(player_has_won=True)),
            human_losses=Count('pk', filter=Q(player_has_won=False)),
            bot_wins=Count('pk', filter=Q(player_has_won=False)),
            bot_losses=Count('pk', filter=Q(player_has_won=True)),
            ties=Count('pk', filter=Q(player_has_won=None)),
            humans_played_rock=Count('pk', filter=Q(player_choice='R')),
            humans_played_paper=Count('pk', filter=Q(player_choice='P')),
            humans_played_scissors=Count('pk', filter=Q(player_choice='S'))
        )
