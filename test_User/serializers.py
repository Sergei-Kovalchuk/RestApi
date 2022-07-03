from test_User.models import Create

from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Create
        fields = ['id', 'surname', 'username', 'patronymic']
