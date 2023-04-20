from rest_framework import serializers
from .models import *


class TeamSerializer(serializers.ModelSerializer):

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



class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = '__all__'

    
