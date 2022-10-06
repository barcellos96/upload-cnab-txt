from rest_framework import serializers

from .models import Documents


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = [
            "id",
            "type",
            "date",
            "value",
            "cpf",
            "card",
            "hour",
            "store_owner",
            "store_name",
        ]