import os
import re
import logging
import datetime
import threading
import traceback

from django.http import FileResponse

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework import exceptions
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .deposit import random as l_random
from .deposit import deposit as l_deposit

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
             dd_mixins.GroupByMixin,
             viewsets.ReadOnlyModelViewSet):
    queryset = l_models.Result.objects.all()
    serializer_class = l_serializers.Result

    permission_classes = []

    filter_class = l_filters.Result
    ordering_fields = "__all__"
    search_fields = ["owner_address"]
    group_by_fields = ["round", "owner_address"]

    @action(methods=["get"], detail=False, url_path="rewards")
    @dd_decorators.parameter("owner_address", str, required=True)
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


class Depositkey(viewsets.ViewSet):
    queryset = l_models.DepositKey.objects.all()
    serializer_class = l_serializers.DepositKey

    permission_classes = []

    @action(methods=["post"], detail=False, url_path="new")
    def c_new(self, request, *args, **kwargs):
        dir_name = l_random.get_dir_name()
        now = datetime.datetime.now()
        timestamp = now.timestamp()
        timestamp_str = str(timestamp)
        timestamp_str = timestamp_str.replace(".", "_")
        dir_name = "deposit_" + timestamp_str + "_" + dir_name
        deposit_key = l_deposit.DepositKey(dir_name)
        try:
            deposit_key.create()
            hex = deposit_key.get_hex()
            keystore_password = deposit_key.get_keystore_password()
        except Exception as exc:
            logger.warning(f"create key failed {traceback.format_exc()}")
            raise exceptions.ParseError(f"create key failed")
        instance = l_models.DepositKey.objects.create(hex=hex, dir_name=dir_name)
        serializer = l_serializers.DepositKey(instance)
        data = serializer.data
        data["keystore_password"] = keystore_password
        return Response(data)

    @action(methods=["get"], detail=False, url_path="download")
    @dd_decorators.parameter("dir_name", str, required=True)
    def c_download(self, request, dir_name, *args, **kwargs):
        deposit_key = l_deposit.DepositKey(dir_name)
        zip_file_path = deposit_key.create_zip()
        # file_name = deposit_key.get_zip_file_path
        file = open(zip_file_path, "rb")
        response = FileResponse(file)
        return response


#     @action(methods=["get"], detail=False, url_path="group-by")
# e    @de(cache_page(60*60*2))
#     def group_by(self, request, *args, **kwargs):
#         super().group_by(request, *args, **kwargs)
