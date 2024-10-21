from rest_framework import serializers


from main_app.models.models import (
    Laboratories
)

from hecoto_backend.users.api.serializers import (
    UserSerializer
)


class LaboratoriesSerializer(serializers.ModelSerializer):
    """
    Serializador de servicios
    """
    class Meta:
        model = Laboratories
        fields = '__all__'
        expandable_fields = {
            'create_user': (UserSerializer),
        }