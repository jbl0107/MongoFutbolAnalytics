from django.db import models
from mongoengine import Document, StringField, ImageField, DateField, IntField, ReferenceField, BooleanField
import mongoengine


class League(models.TextChoices):
    SPANISHLEAGUE = "LaLiga"
    ENGLISHLEAGUE = "Premier League"
    FRENCHLEAGUE = "Ligue 1"
    ITALIANLEAGUE = "Serie A"
    GERMANLEAGUE = "Bundesliga"


class GoodLeg(models.TextChoices):
    LEFTFOOTED = "Zurdo"
    RIGHTFOOTED = "Diestro"
    BOTHFEET = "Ambidiestro"


class GoalType(models.TextChoices):
    HEAD = "De cabeza"
    PENALTY = "Penalti"
    FREESHOT = "Tiro libre"
    CORNER = "Corner"
    CHILEAN= "Chilena"
    LEFTLEG = "Pierna izquierda"
    RIGHLEG = "Pierna derecha"
    OUTSIDE = "Fuera del áera"
    INSIDE = "Dentro del área"


class TitleName(models.TextChoices):
    CHAMPIONS = "Champions League"
    EUROPE = "Europa League"
    SPANISHLEAGUE = "LaLiga"
    KINGCUP= "Copa del rey"
    ENGLISHLEAGUE = "Premier League"
    COMMUNITY = "Community shield"
    FRENCHLEAGUE = "Ligue 1"
    COUPE = "Coupe de la Ligue"
    ITALIANLEAGUE = "Serie A"
    COPPA = "Coppa Italia"
    GERMANLEAGUE = "Bundesliga"
    GERMANCOPE = "DFB-Pokal"





class Team(Document):
    name = StringField(max_length=100, required=True, unique=True)
    shield = ImageField(required=True)
    foundationDate = DateField(required=True)
    league = StringField(max_length=16 ,choices=League.choices, default="-", required=True)
    actualPosition = IntField(required=True, min_value=1, max_value=20)
    pastPosition = IntField(required=True, min_value=1, max_value=20)


    def __str__(self):
        return self.name
    



class Title(Document):
    name = StringField(max_length=25 ,choices=TitleName.choices, default="-", required=True)
    team = ReferenceField(Team, reverse_delete_rule=mongoengine.DO_NOTHING, required=True)
    year = IntField(required=True, min_value=1888, max_value=2023)

    meta = {
        'indexes': [
            {'fields': ('name', 'year'), 'unique': True},
            {'fields': ('name', 'team', 'year'), 'unique': True}
        ]
    }

    def __str__(self):
        return self.name




class Player(Document):
    name = StringField(max_length=100, required=True, unique=True)
    dorsal = IntField(required=True)
    goodLeg = StringField(max_length=12 ,choices=GoodLeg.choices, default="-", required=True)
    team = ReferenceField(Team, reverse_delete_rule=mongoengine.DO_NOTHING, required=True)
    gamesPlayed = IntField(required=True, default=0)
    photo = ImageField()

    meta = {
        'indexes': [
            {'fields': ('dorsal', 'team'), 'unique': True}
        ]
    }

    def __str__(self):
        return f'{self.name}'
    



class Goal(Document):
    player = ReferenceField(Player, reverse_delete_rule=mongoengine.CASCADE, required=True)
    team = ReferenceField(Team, reverse_delete_rule=mongoengine.CASCADE, required=True)
    minute = IntField(required=True, max_value=120)
    type = StringField(max_length=20 ,choices=GoalType.choices, default="-", required=True)
    assistant = ReferenceField(Player, reverse_delete_rule=mongoengine.CASCADE)
    local = BooleanField(required=True)
    year = IntField(required=True, min_value=1888, max_value=2023)
    competition = StringField(max_length=25 ,choices=TitleName.choices, default="-", required=True)

    meta = {
        'indexes': [
            {'fields': ('player', 'team', 'year', 'competition', 'minute'), 'unique': True}
        ]
    }

    def __str__(self):
        return f'{self.player} marcó un gol a el {self.team}'