
from .. import models as l_models


class AddressReward:

    def __init__(self, address):
        self._address = address

    # def _get_results(self):
    #     qs = l_models.Result.objects.filter(owner_address=self._address)

    def get_all_rewards(self):
        qs = l_models.Result.objects.filter(owner_address=self._address)
        rewards_overview = [
            {"title": "validators"} + dict(qs.values("validators"))
        ]
        return rewards_overview

    def get_round_rewards(self, round):
        pass
