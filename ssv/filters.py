
from django_filters import rest_framework as filters

from . import models as l_models


class Result(filters.FilterSet):

    class Meta:
        model = l_models.Result
        fields = {
            "round": ["exact"],
            "owner_address": ["exact"],
        }


