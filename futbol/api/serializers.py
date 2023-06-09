from rest_framework_mongoengine import serializers
from .models import *


class TeamSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Team
        fields = '__all__'
        extra_kwargs = {('name', 'foundationDate', 'league'): {'write_only': True}}


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['name'] = instance.name
        representation['foundationDate'] = instance.foundationDate
        representation['league'] = instance.league
        return representation



class TitleSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Title
        fields = '__all__'

    

class PlayerSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Player
        fields = '__all__'



class GoalSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Goal
        fields = '__all__'