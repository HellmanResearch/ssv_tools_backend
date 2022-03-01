
from rest_framework import serializers as l_serializers

from . import models as l_models


class Result(l_serializers.ModelSerializer):

    class Meta:
        model = l_models.Result
        fields = "__all__"
