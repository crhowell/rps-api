from django.db import models
from django.contrib.auth import get_user_model


from . import managers

User = get_user_model()


class Bot(models.Model):
    LEVELS = (
        ('R', 'Random'), 
        ('S', 'Smarter'),
    )
    name = models.CharField(max_length=100, blank=True, default='')
    level = models.CharField(max_length=1, choices=LEVELS, default='R')

    def save(self, *args, **kwargs):
        level = self.get_level_display()
        if not self.name:
            self.name = f'{level} Bot'
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.name} #{self.id}'


class GameRound(models.Model):
    CHOICES = (
        ('R', 'Rock'),
        ('P', 'Paper'),
        ('S', 'Scissors'),
    )
    player_choice = models.CharField(max_length=1, choices=CHOICES)
    bot_choice = models.CharField(max_length=1, choices=CHOICES)
    player_has_won = models.BooleanField(default=None, null=True)

    creator = models.ForeignKey(User, related_name='game_rounds',
                                on_delete=models.CASCADE)
    bot = models.ForeignKey(Bot, related_name='game_rounds',
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Replace inherited Model Manager with one similar but modified.
    objects = managers.GameRoundManager()
    def __str__(self):
        return f'Game {self.id}'

