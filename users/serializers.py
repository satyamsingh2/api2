from rest_framework import serializers
from users.models import Users#, LANGUAGE_CHOICES, STYLE_CHOICES


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'company_name', 'city', 'state',
         'zip', 'email', 'web', 'age']
    
    def create(self, validated_data):
        return Users(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.web = validated_data.get('web', instance.content)
        return instance

class UsersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'age']