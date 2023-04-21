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
    path('players/team/<int:team_id>/number', players_number_team_detail_api_view, name='players_number_team_detail_api'),
    path('players/team/<int:team_id>/<str:good_leg>', players_goodLeg_detail_api_view, name='players_goodLeg_detail_api'),
    
    
    path('goals/', goal_api_view, name='goal_api'),
    path('goals/<int:id>', goal_detail_api_view, name='goal_detail_api'),
    path('goals/player/<int:player_id>', goals_player_detail_api_view, name='goals_player_detail_api'),
    path('goals/player/<int:player_id>/number', goals_number_player_detail_api_view, name='goals_number_player_detail_api'),
    path('goals/player/<int:player_id>/<str:type>', goals_type_player_detail_api_view, name='goals_type_player_detail_api'),
    path('goals/player/<int:player_id>/<str:type>/number', goals_number_type_player_detail_api_view, name='goals_number_type_player_detail_api'),
    path('goals/player/<int:player_id>/competition/<str:competition>', goals_competition_player_detail_api_view, name='goals_competition_player_detail_api'),
    path('goals/player/<int:player_id>/competition/<str:competition>/number', goals_number_competition_player_detail_api_view, name='goals_number_competition_player_detail_api'),
    path('goals/competition/<str:competition>', goals_competition_detail_api_view, name='goals_competition_detail_api'),
    path('goals/competition/<str:competition>/number', goals_number_competition_detail_api_view, name='goals_number_competition_detail_api'),
    path('goals/year/<int:year>', goals_year_detail_api_view, name='goals_year_detail_api'),
    path('goals/year/<int:year>/number', goals_number_year_detail_api_view, name='goals_number_year_detail_api'),
    path('goals/competition/<str:competition>/year/<int:year>', goals_year_competition_detail_api_view, name='goals_year_competition_detail_api'),
    path('goals/competition/<str:competition>/year/<int:year>/number', goals_number_year_competition_detail_api_view, name='goals_number_year_competition_detail_api'),
    path('goals/player/<int:player_id>/year/<int:year>', goals_player_year_detail_api_view, name='goals_player_year_detail_api'),
    path('goals/player/<int:player_id>/year/<int:year>/number', goals_player_year_number_detail_api_view, name='goals_player_year_number_detail_api'),
    path('goals/player/<int:player_id>/competition/<str:competition>/year/<int:year>', goals_player_competition_year_detail_api_view, name='goals_competition_year_detail_api'),
    path('goals/player/<int:player_id>/competition/<str:competition>/year/<int:year>/number', goals_player_competition_year_number_detail_api_view, name='goals_competition_year_number_detail_api'),
    path('goals/assistances/<int:player_id>/', goals_assistant_detail_api_view, name='goals_assistant_detail_api'),
    path('goals/assistances/<int:player_id>/number', goals_number_assistant_detail_api_view, name='goals_number_assistant_detail_api'),
    path('goals/assistances/<int:player_id>/<str:competition>', goals_assistant_competition_detail_api_view, name='goals_assistant_competition_detail_api'),
    path('goals/assistances/<int:player_id>/<str:competition>/number', goals_number_assistant_competition_detail_api_view, name='goals_number_assistant_competition_detail_api'),
    path('goals/assistances/<int:player_id>/year/<int:year>', goals_assistant_year_detail_api_view, name='goals_assistant_year_detail_api'),
    path('goals/assistances/<int:player_id>/year/<int:year>/number', goals_number_assistant_year_detail_api_view, name='goals_number_assistant_year_detail_api'),
    path('goals/assistances/<int:player_id>/year/<int:year>/competition/<str:competition>', goals_assistant_year_competition_detail_api_view, name='goals_assistant_year_competition_detail_api'),
    path('goals/assistances/<int:player_id>/year/<int:year>/competition/<str:competition>/number', goals_number_assistant_year_competition_detail_api_view, name='goals_number_assistant_year_competition_detail_api'),
    path('goals/received/<int:team_id>', goals_received_detail_api_view, name='goals_received_detail_api'),
    path('goals/received/<int:team_id>/number', goals_number_received_detail_api_view, name='goals_number_received_detail_api'),
    path('goals/received/<int:team_id>/competition/<str:competition>', goals_received_competition_detail_api_view, name='goals_received_competition_detail_api'),
    path('goals/received/<int:team_id>/competition/<str:competition>/number', goals_number_received_competition_detail_api_view, name='goals_number_received_competition_detail_api'),
    path('goals/received/<int:team_id>/year/<int:year>', goals_received_year_detail_api_view, name='goals_received_year_detail_api'),
    path('goals/received/<int:team_id>/year/<int:year>/number', goals_number_received_year_detail_api_view, name='goals_number_received_year_detail_api'),
    path('goals/received/<int:team_id>/year/<int:year>/competition/<str:competition>', goals_received_year_competition_detail_api_view, name='goals_received_year_competition_detail_api'),
    path('goals/received/<int:team_id>/year/<int:year>/competition/<str:competition>/number', goals_number_received_year_competition_detail_api_view, name='goals_number_received_year_competition_detail_api'),


]

