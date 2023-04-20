from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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





class Team(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    shield = models.ImageField(upload_to='shields/', null=False, blank=False)
    foundationDate = models.DateField(null=False, blank=False)
    league = models.CharField(max_length=16 ,choices=League.choices, default="-", null=False)
    actualPosition = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(20)])
    pastPosition = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(20)])


    def __str__(self):
        return self.name
    



class Title(models.Model):
    name = models.CharField(max_length=25 ,choices=TitleName.choices, default="-", null=False)
    team =  models.ForeignKey(Team, on_delete=models.DO_NOTHING, null=False, blank=False, related_name='titles')
    year = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1888), MaxValueValidator(2023)])


    class Meta:
        unique_together = (('name', 'year'), ('name', 'team', 'year'))

    def __str__(self):
        return self.name





class Player(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    dorsal = models.IntegerField(null=False, blank=False)
    goodLeg = models.CharField(max_length=12 ,choices=GoodLeg.choices, default="-", null=False)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, null=False, blank=False, related_name='players')
    photo = models.ImageField(upload_to='players/', null=True, blank=True)

    class Meta:
        unique_together = ('dorsal', 'team')

    def __str__(self):
        return f'{self.name} juega en el equipo {self.team}'
    



class Goal(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=False, blank=False, related_name='goals') 
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, blank=False, related_name='goals_conceded')
    minute = models.IntegerField(null=False, blank=False, validators=[MaxValueValidator(120)])
    type = models.CharField(max_length=20 ,choices=GoalType.choices, default="-", null=False)
    assistant = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True, related_name='assists')

    def __str__(self):
        return f'{self.player} marcó un gol a el {self.team}'