from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from .models import *
from .serializers import *


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