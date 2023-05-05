from api.models import Team, Player, Title, Goal
from mongoengine import connect



connect(db='workDB', host='mongodb+srv://cbd17:ZnVVRUDzgE8Khskr@cbdcluster.mzw9cbr.mongodb.net/?retryWrites=true&w=majority')


# Crear y guardar documentos en la base de datos
team = Team(name='Real Madrid', shield='media/shields/Real_Madrid.jpg', foundationDate='1902-03-06', league='LaLiga', actualPosition=2, pastPosition=1)
team.save()

title = Title(name='LaLiga', team=team, year=2022)
title.save()

player = Player(name='Modric', dorsal=10, goodLeg='Diestro', team=team, gamesPlayed=378)
player.save()


goal = Goal(player=player, team=team, minute=30, type='De cabeza', assistant=player, local=True, year=2022, competition='Copa del rey')
goal.save()
