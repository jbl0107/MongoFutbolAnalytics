from django.urls import path
from .apis import *


urlpatterns = [
    path('teams/', team_api_view, name='team_api'),
    path('teams/<int:id>', team_detail_api_view, name='team_detail_api'),
    path('titles/', title_api_view, name='title_api'),
    path('titles/<int:id>', title_detail_api_view, name='title_detail_api'),
    path('titles/team/<int:team_id>', titles_team_detail_api_view, name='titles_team_detail_api'),
    path('titles/number/team/<int:team_id>', titles_team_number_detail_api_view, name='titles_team_number_detail_api'),
    path('titles/team/<int:team_id>/<str:title_name>', titles_team_type_detail_api_view, name='titles_team_type_detail_api'),
    path('titles/team/<int:team_id>/<str:title_name>/number', titles_team_type_number_detail_api_view, name='titles_team_type_number_detail_api'),
    path('players/', player_api_view, name='player_api'),
    path('players/<int:id>', player_detail_api_view, name='player_detail_api'),
    path('players/team/<int:team_id>', players_team_detail_api_view, name='players_team_detail_api'),
    path('players/team/number/<int:team_id>', players_number_team_detail_api_view, name='players_number_team_detail_api'),
    

]

