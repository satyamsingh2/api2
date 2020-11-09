from rest_framework import serializers
from users.models import Users#, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework.serializers import ValidationError


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'company_name', 'city', 'state',
         'zip', 'email', 'web', 'age']
    
   
    def to_representation(self, instance):
        ret = super(UsersSerializer, self).to_representation(instance)
        ret['first_name'] = ret['first_name'].upper()
        ret['last_name'] = ret['last_name'].upper()
        return ret

    def validate_city(self, city):
        if not "delhi" in city.lower() and not"agra" in city.lower() :
            raise serializers.ValidationError({"please enter the city again"})
        return city

class UsersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'age']