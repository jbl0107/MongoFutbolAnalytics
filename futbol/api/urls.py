from django.urls import path
from .apis import *
from .views import index, teams, players, titles, goals


urlpatterns = [
    path('', index, name='index'),
    path('teams_view/', teams, name='teams'),
    path('players_view/', players, name='players'),
    path('titles_view/', titles, name='titles'),
    path('goals_view/', goals, name='goals'),
    
    path('teams/', team_api_view, name='team_api'),
    path('teams/<str:id>', team_detail_api_view, name='team_detail_api'),
    path('teams/<str:title_name>/<int:year>/', team_what_win_detail_api_view, name='time_what_win_detail_api'),


    path('titles/', title_api_view, name='title_api'),
    path('titles/<str:id>', title_detail_api_view, name='title_detail_api'),
    path('titles/team/<str:team_id>', titles_team_detail_api_view, name='titles_team_detail_api'),
    path('titles/number/team/<str:team_id>', titles_team_number_detail_api_view, name='titles_team_number_detail_api'),
    path('titles/team/<str:team_id>/<str:title_name>', titles_team_type_detail_api_view, name='titles_team_type_detail_api'),
    path('titles/team/<str:team_id>/<str:title_name>/number', titles_team_type_number_detail_api_view, name='titles_team_type_number_detail_api'),

    path('players/', player_api_view, name='player_api'),
    path('players/<str:id>', player_detail_api_view, name='player_detail_api'),
    path('players/team/<str:team_id>', players_team_detail_api_view, name='players_team_detail_api'),
    path('players/team/<str:team_id>/number', players_number_team_detail_api_view, name='players_number_team_detail_api'),
    path('players/team/<str:team_id>/<str:good_leg>', players_goodLeg_detail_api_view, name='players_goodLeg_detail_api'),
    
    
    path('goals/', goal_api_view, name='goal_api'),
    path('goals/<str:id>', goal_detail_api_view, name='goal_detail_api'),
    path('goals/player/<str:player_id>', goals_player_detail_api_view, name='goals_player_detail_api'),
    path('goals/player/<str:player_id>/number', goals_number_player_detail_api_view, name='goals_number_player_detail_api'),
    path('goals/player/<str:player_id>/<str:type>', goals_type_player_detail_api_view, name='goals_type_player_detail_api'),
    path('goals/player/<str:player_id>/<str:type>/number', goals_number_type_player_detail_api_view, name='goals_number_type_player_detail_api'),
    path('goals/player/<str:player_id>/competition/<str:competition>', goals_competition_player_detail_api_view, name='goals_competition_player_detail_api'),
    path('goals/player/<str:player_id>/competition/<str:competition>/number', goals_number_competition_player_detail_api_view, name='goals_number_competition_player_detail_api'),
    path('goals/competition/<str:competition>', goals_competition_detail_api_view, name='goals_competition_detail_api'),
    path('goals/competition/<str:competition>/number', goals_number_competition_detail_api_view, name='goals_number_competition_detail_api'),
    path('goals/year/<int:year>', goals_year_detail_api_view, name='goals_year_detail_api'),
    path('goals/year/<int:year>/number', goals_number_year_detail_api_view, name='goals_number_year_detail_api'),
    path('goals/competition/<str:competition>/year/<int:year>', goals_year_competition_detail_api_view, name='goals_year_competition_detail_api'),
    path('goals/competition/<str:competition>/year/<int:year>/number', goals_number_year_competition_detail_api_view, name='goals_number_year_competition_detail_api'),
    path('goals/player/<str:player_id>/year/<int:year>', goals_player_year_detail_api_view, name='goals_player_year_detail_api'),
    path('goals/player/<str:player_id>/year/<int:year>/number', goals_player_year_number_detail_api_view, name='goals_player_year_number_detail_api'),
    path('goals/player/<str:player_id>/competition/<str:competition>/year/<int:year>', goals_player_competition_year_detail_api_view, name='goals_competition_year_detail_api'),
    path('goals/player/<str:player_id>/competition/<str:competition>/year/<int:year>/number', goals_player_competition_year_number_detail_api_view, name='goals_competition_year_number_detail_api'),
    path('goals/assistances/<str:player_id>/', goals_assistant_detail_api_view, name='goals_assistant_detail_api'),
    path('goals/assistances/<str:player_id>/number', goals_number_assistant_detail_api_view, name='goals_number_assistant_detail_api'),
    path('goals/assistances/<str:player_id>/<str:competition>', goals_assistant_competition_detail_api_view, name='goals_assistant_competition_detail_api'),
    path('goals/assistances/<str:player_id>/<str:competition>/number', goals_number_assistant_competition_detail_api_view, name='goals_number_assistant_competition_detail_api'),
    path('goals/assistances/<str:player_id>/year/<int:year>', goals_assistant_year_detail_api_view, name='goals_assistant_year_detail_api'),
    path('goals/assistances/<str:player_id>/year/<int:year>/number', goals_number_assistant_year_detail_api_view, name='goals_number_assistant_year_detail_api'),
    path('goals/assistances/<str:player_id>/year/<int:year>/competition/<str:competition>', goals_assistant_year_competition_detail_api_view, name='goals_assistant_year_competition_detail_api'),
    path('goals/assistances/<str:player_id>/year/<int:year>/competition/<str:competition>/number', goals_number_assistant_year_competition_detail_api_view, name='goals_number_assistant_year_competition_detail_api'),
    path('goals/received/<str:team_id>', goals_received_detail_api_view, name='goals_received_detail_api'),
    path('goals/received/<str:team_id>/number', goals_number_received_detail_api_view, name='goals_number_received_detail_api'),
    path('goals/received/<str:team_id>/competition/<str:competition>', goals_received_competition_detail_api_view, name='goals_received_competition_detail_api'),
    path('goals/received/<str:team_id>/competition/<str:competition>/number', goals_number_received_competition_detail_api_view, name='goals_number_received_competition_detail_api'),
    path('goals/received/<str:team_id>/year/<int:year>', goals_received_year_detail_api_view, name='goals_received_year_detail_api'),
    path('goals/received/<str:team_id>/year/<int:year>/number', goals_number_received_year_detail_api_view, name='goals_number_received_year_detail_api'),
    path('goals/received/<str:team_id>/year/<int:year>/competition/<str:competition>', goals_received_year_competition_detail_api_view, name='goals_received_year_competition_detail_api'),
    path('goals/received/<str:team_id>/year/<int:year>/competition/<str:competition>/number', goals_number_received_year_competition_detail_api_view, name='goals_number_received_year_competition_detail_api'),
    path('goals/team/<str:team_id>/scored', goals_scored_detail_api_view, name='goals_scored_detail_api_view'),
    path('goals/team/<str:team_id>/scored/number', goals_number_scored_detail_api_view, name='goals_number_scored_detail_api_view'),
    path('goals/team/<str:team_id>/scored/year/<int:year>', goals_scored_year_detail_api_view, name='goals_scored_year_detail_api_view'),
    path('goals/team/<str:team_id>/scored/year/<int:year>/number', goals_number_scored_year_detail_api_view, name='goals_number_scored_year_detail_api_view'),
    path('goals/team/<str:team_id>/scored/competition/<str:competition>', goals_scored_competition_detail_api_view, name='goals_scored_year_detail_api_view'),
    path('goals/team/<str:team_id>/scored/competition/<str:competition>/number', goals_number_scored_competition_detail_api_view, name='goals_number_scored_year_detail_api_view'),
    path('goals/team/<str:team_id>/scored/year/<int:year>/competition/<str:competition>', goals_scored_year_competition_detail_api_view, name='goals_scored_year_competition_detail_api_view'),
    path('goals/team/<str:team_id>/scored/year/<int:year>/competition/<str:competition>/number', goals_number_scored_year_competition_detail_api_view, name='goals_number_scored_year_competition_detail_api_view'),


]

