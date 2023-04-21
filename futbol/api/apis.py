from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *
from .serializers import *


#Team

@api_view(['GET', 'POST'])
def team_api_view(request):

    if request.method == 'GET':

        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        serializer = TeamSerializer(data = data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def team_detail_api_view(request, id):

    # queryset
    team = Team.objects.filter(id=id).first()

    # validacion
    if team:

        if request.method == 'GET':
            serializer = TeamSerializer(team)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':

            name = team.name
            foundationDate = team.foundationDate
            league = team.league
            shield = team.shield

            data = request.data

            mutable_data = data.copy()

            mutable_data['name'] = name
            mutable_data['foundationDate'] = foundationDate 
            mutable_data['league'] = league

            if 'shield' not in mutable_data:
                mutable_data['shield'] = shield

            serializer = TeamSerializer(team, data = mutable_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            team.delete()
            return Response({'message':"Equipo eliminado correctamente!"}, status=status.HTTP_200_OK)

    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)


###########################################################################################################################




#Title

@api_view(['GET', 'POST'])
def title_api_view(request):

    if request.method == 'GET':

        titles = Title.objects.all()
        serializer = TitleSerializer(titles, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        serializer = TitleSerializer(data = data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'DELETE'])
def title_detail_api_view(request, id):

    # queryset
    title = Title.objects.filter(id=id).first()

    # validacion
    if title:

        if request.method == 'GET':
            serializer = TitleSerializer(title)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            title.delete()
            return Response({'message':"Título eliminado correctamente!"}, status=status.HTTP_200_OK)

    return Response({'message':"No se ha encontrado un titulo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def titles_team_detail_api_view(request, team_id):

    team = Team.objects.filter(id=team_id).first()

    if team:

        if request.method == 'GET':
            titles = Title.objects.filter(team=team)
            serializer = TitleSerializer(titles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def titles_team_number_detail_api_view(request, team_id):
        
    team = Team.objects.filter(id=team_id).first()

    if team:

        if request.method == 'GET':
            titles = Title.objects.filter(team=team)
            serializer = TitleSerializer(titles, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)


    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def titles_team_type_detail_api_view(request, team_id, title_name):

    team = Team.objects.filter(id=team_id).first()

    if team:

        if request.method == 'GET':
            title_name = title_name.replace('-', ' ')

            titles = Title.objects.filter(team=team, name=title_name)
            serializer = TitleSerializer(titles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def titles_team_type_number_detail_api_view(request, team_id, title_name):

    team = Team.objects.filter(id=team_id).first()

    if team:

        if request.method == 'GET':
            title_name = title_name.replace('-', ' ')

            titles = Title.objects.filter(team=team, name=title_name)
            serializer = TitleSerializer(titles, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)


    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)


########################################################################################################################




#Player

@api_view(['GET', 'POST'])
def player_api_view(request):

    if request.method == 'GET':

        teams = Player.objects.all()
        serializer = PlayerSerializer(teams, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PlayerSerializer(data = data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def player_detail_api_view(request, id):

    # queryset
    player = Player.objects.filter(id=id).first()

    # validacion
    if player:

        if request.method == 'GET':
            serializer = PlayerSerializer(player)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            data = request.data
            serializer = PlayerSerializer(player, data = data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            player.delete()
            return Response({'message':"Jugador eliminado correctamente!"}, status=status.HTTP_200_OK)

    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def players_team_detail_api_view(request, team_id):

    team = Team.objects.filter(id=team_id).first()

    if team:

        if request.method == 'GET':

            players = Player.objects.filter(team=team)
            serializer = PlayerSerializer(players, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def players_number_team_detail_api_view(request, team_id):

    team = Team.objects.filter(id=team_id).first()

    if team:

        if request.method == 'GET':

            players = Player.objects.filter(team=team)
            serializer = PlayerSerializer(players, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)


    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def players_goodLeg_detail_api_view(request, team_id, good_leg):

    team = Team.objects.filter(id=team_id).first()

    if team:

        if request.method == 'GET':

            players = Player.objects.filter(team=team, goodLeg=good_leg)
            serializer = PlayerSerializer(players, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)


###########################################################################################################################




#Goal

@api_view(['GET', 'POST'])
def goal_api_view(request):

    if request.method == 'GET':

        goals = Goal.objects.all()
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data

        if data.get('player') == data.get('assistant'):
            return Response({'message':"Un jugador no puede asistirse a sí mismo"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = GoalSerializer(data = data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'DELETE'])
def goal_detail_api_view(request, id):

    # queryset
    goal = Goal.objects.filter(id=id).first()

    # validacion
    if goal:

        if request.method == 'GET':
            serializer = GoalSerializer(goal)
            return Response(serializer.data, status=status.HTTP_200_OK)


        elif request.method == 'DELETE':
            goal.delete()
            return Response({'message':"Gol eliminado correctamente!"}, status=status.HTTP_200_OK)

    return Response({'message':"No se ha encontrado un gol con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_player_detail_api_view(request, player_id):

    player = Player.objects.filter(id=player_id).first()

    if player:

        if request.method == 'GET':

            goals = Goal.objects.filter(player=player)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def goals_number_player_detail_api_view(request, player_id):

    player = Player.objects.filter(id=player_id).first()

    if player:

        if request.method == 'GET':

            goals = Goal.objects.filter(player=player)
            serializer = GoalSerializer(goals, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)


    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_type_player_detail_api_view(request, player_id, type):

    player = Player.objects.filter(id=player_id).first()

    if player:

        if request.method == 'GET':
            type = type.replace('-', ' ')

            goals = Goal.objects.filter(player=player, type=type)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def goals_number_type_player_detail_api_view(request, player_id, type):

    player = Player.objects.filter(id=player_id).first()
    
    if player:

        if request.method == 'GET':
            type = type.replace('-', ' ')

            goals = Goal.objects.filter(player=player, type=type)
            serializer = GoalSerializer(goals, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)


    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def goals_competition_player_detail_api_view(request, player_id, competition):

    player = Player.objects.filter(id=player_id).first()
    print(player)

    

    if player:
        
        if request.method == 'GET':
            competition = competition.replace('-', ' ')

            goals = Goal.objects.filter(player=player, competition=competition)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_number_competition_player_detail_api_view(request, player_id, competition):

    player = Player.objects.filter(id=player_id).first()

    if player:
        
        if request.method == 'GET':
            competition = competition.replace('-', ' ')

            goals = Goal.objects.filter(player=player, competition=competition)
            serializer = GoalSerializer(goals, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)


    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_competition_detail_api_view(request, competition):

    
    if request.method == 'GET':
        competition = competition.replace('-', ' ')

        goals = Goal.objects.filter(competition=competition)
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def goals_number_competition_detail_api_view(request, competition):

    
    if request.method == 'GET':
        competition = competition.replace('-', ' ')

        goals = Goal.objects.filter(competition=competition)
        serializer = GoalSerializer(goals, many=True)
        return Response(len(serializer.data), status=status.HTTP_200_OK)
    



@api_view(['GET'])
def goals_year_detail_api_view(request, year):

    
    if request.method == 'GET':

        goals = Goal.objects.filter(year=year)
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def goals_number_year_detail_api_view(request, year):

    
    if request.method == 'GET':

        goals = Goal.objects.filter(year=year)
        serializer = GoalSerializer(goals, many=True)
        return Response(len(serializer.data), status=status.HTTP_200_OK)
    




@api_view(['GET'])
def goals_year_competition_detail_api_view(request, year, competition):

    
    if request.method == 'GET':
        competition = competition.replace('-', ' ')

        goals = Goal.objects.filter(year=year, competition=competition)
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def goals_number_year_competition_detail_api_view(request, year, competition):

    
    if request.method == 'GET':
        competition = competition.replace('-', ' ')

        goals = Goal.objects.filter(year=year, competition=competition)
        serializer = GoalSerializer(goals, many=True)
        return Response(len(serializer.data), status=status.HTTP_200_OK)
    




@api_view(['GET'])
def goals_player_year_detail_api_view(request, player_id, year):

    player = Player.objects.filter(id=player_id).first()

    if player:

        if request.method == 'GET':

            goals = Goal.objects.filter(player=player, year=year)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_player_year_number_detail_api_view(request, player_id, year):
    
    player = Player.objects.filter(id=player_id).first()

    if player:
    
        if request.method == 'GET':

            goals = Goal.objects.filter(player=player, year=year)
            serializer = GoalSerializer(goals, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def goals_player_competition_year_detail_api_view(request, player_id, year, competition):

    player = Player.objects.filter(id=player_id).first()

    if player:

        if request.method == 'GET':
            competition = competition.replace('-', ' ')
            
            goals = Goal.objects.filter(player=player, year=year, competition=competition)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_player_competition_year_number_detail_api_view(request, player_id, year, competition):
    
    player = Player.objects.filter(id=player_id).first()

    if player:
    
        if request.method == 'GET':
            competition = competition.replace('-', ' ')

            goals = Goal.objects.filter(player=player, year=year, competition=competition)
            serializer = GoalSerializer(goals, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def goals_assistant_detail_api_view(request, player_id):
    
    player = Player.objects.filter(id=player_id).first()

    if player:
    
        if request.method == 'GET':
            goals = Goal.objects.filter(assistant=player)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_number_assistant_detail_api_view(request, player_id):
    
    player = Player.objects.filter(id=player_id).first()

    if player:
    
        if request.method == 'GET':
            goals = Goal.objects.filter(assistant=player)
            serializer = GoalSerializer(goals, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def goals_assistant_competition_detail_api_view(request, player_id, competition):
    
    player = Player.objects.filter(id=player_id).first()

    if player:
    
        if request.method == 'GET':
            competition = competition.replace('-', ' ')
            goals = Goal.objects.filter(assistant=player, competition=competition)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_number_assistant_competition_detail_api_view(request, player_id, competition):
    
    player = Player.objects.filter(id=player_id).first()

    if player:
    
        if request.method == 'GET':
            competition = competition.replace('-', ' ')
            goals = Goal.objects.filter(assistant=player, competition=competition)
            serializer = GoalSerializer(goals, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_assistant_year_detail_api_view(request, player_id, year):
    
    player = Player.objects.filter(id=player_id).first()

    if player:
    
        if request.method == 'GET':
            goals = Goal.objects.filter(assistant=player, year=year)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_number_assistant_year_detail_api_view(request, player_id, year):
    
    player = Player.objects.filter(id=player_id).first()

    if player:
    
        if request.method == 'GET':
            goals = Goal.objects.filter(assistant=player, year=year)
            serializer = GoalSerializer(goals, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)






@api_view(['GET'])
def goals_assistant_year_competition_detail_api_view(request, player_id, year, competition):
    
    player = Player.objects.filter(id=player_id).first()

    if player:
    
        if request.method == 'GET':
            competition = competition.replace('-', ' ')
            goals = Goal.objects.filter(assistant=player, year=year, competition=competition)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_number_assistant_year_competition_detail_api_view(request, player_id, year, competition):
    
    player = Player.objects.filter(id=player_id).first()

    if player:
    
        if request.method == 'GET':
            competition = competition.replace('-', ' ')
            goals = Goal.objects.filter(assistant=player, year=year, competition=competition)
            serializer = GoalSerializer(goals, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un jugador con estos datos"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def goals_received_detail_api_view(request, team_id):
    
    team = Team.objects.filter(id=team_id).first()

    if team:
    
        if request.method == 'GET':
            goals = Goal.objects.filter(team=team)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_number_received_detail_api_view(request, team_id):
    
    team = Team.objects.filter(id=team_id).first()

    if team:
    
        if request.method == 'GET':
            goals = Goal.objects.filter(team=team)
            serializer = GoalSerializer(goals, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def goals_received_competition_detail_api_view(request, team_id, competition):
    
    team = Team.objects.filter(id=team_id).first()

    if team:
    
        if request.method == 'GET':
            competition = competition.replace('-', ' ')
            goals = Goal.objects.filter(team=team, competition=competition)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_number_received_competition_detail_api_view(request, team_id, competition):
    
    team = Team.objects.filter(id=team_id).first()

    if team:
    
        if request.method == 'GET':
            competition = competition.replace('-', ' ')
            goals = Goal.objects.filter(team=team, competition=competition)
            serializer = GoalSerializer(goals, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_received_year_detail_api_view(request, team_id, year):
    
    team = Team.objects.filter(id=team_id).first()

    if team:
    
        if request.method == 'GET':
            goals = Goal.objects.filter(team=team, year=year)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_number_received_year_detail_api_view(request, team_id, year):
    
    team = Team.objects.filter(id=team_id).first()

    if team:
    
        if request.method == 'GET':
            goals = Goal.objects.filter(team=team, year=year)
            serializer = GoalSerializer(goals, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_received_year_competition_detail_api_view(request, team_id, year, competition):
    
    team = Team.objects.filter(id=team_id).first()

    if team:
    
        if request.method == 'GET':
            competition = competition.replace('-', ' ')
            goals = Goal.objects.filter(team=team, year=year, competition=competition)
            serializer = GoalSerializer(goals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def goals_number_received_year_competition_detail_api_view(request, team_id, year, competition):
    
    team = Team.objects.filter(id=team_id).first()

    if team:
    
        if request.method == 'GET':
            competition = competition.replace('-', ' ')
            goals = Goal.objects.filter(team=team, year=year, competition=competition)
            serializer = GoalSerializer(goals, many=True)
            return Response(len(serializer.data), status=status.HTTP_200_OK)
        

    return Response({'message':"No se ha encontrado un equipo con estos datos"}, status=status.HTTP_400_BAD_REQUEST)