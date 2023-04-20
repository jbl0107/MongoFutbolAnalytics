from django.urls import path
from .apis import *


urlpatterns = [
    path('teams/', team_api_view, name='team_api'),
    path('teams/<int:id>', team_detail_api_view, name='team_detail_api'),
]
