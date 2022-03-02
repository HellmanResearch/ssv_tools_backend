import os
import re
import logging
import threading

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework import exceptions

import devops_django as l_devops_django
from devops_django import mixins as dd_mixins
from devops_django import decorators as dd_decorators

from . import models as l_models
from . import serializers as l_serializers
from . import filters as l_filters

from .work import reward as l_reward

logger = logging.getLogger(__name__)


class Result(dd_mixins.AggregationMixin,
             dd_mixins.CountMixin,
             viewsets.ReadOnlyModelViewSet):
    queryset = l_models.Result.objects.all()
    serializer_class = l_serializers.Result

    permission_classes = []

    filter_class = l_filters.Result

    @action(methods=["get"], detail=False, url_path="rewards")
    @dd_decorators.parameter("owner_address", str)
    def rewards(self, request, owner_address, *args, **kwargs):
        # try:
        #     result = l_models.Result.objects.filter(owner_address=owner_address)
        # except l_models.Result.DoesNotExist:
        #     raise exceptions.NotFound(f"owner_address: {owner_address} not found")
        is_correct = re.match("^0x[0-9a-fA-F]{40}$", owner_address)
        if is_correct is None:
            raise exceptions.ParseError("wallet address error")
        qs = l_models.Result.objects.filter(owner_address=owner_address)
        if len(qs) == 0:
            raise exceptions.NotFound(f"{owner_address} not in the rewards")
        address_reward = l_reward.AddressReward(owner_address)
        data = address_reward.get_all_rewards()
        res_data = {"results": data}
        return Response(res_data)
