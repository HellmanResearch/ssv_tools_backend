from .. import models as l_models
from .. import serializers as l_serializers


class AddressReward:

    def __init__(self, address):
        self._address = address

    # def _get_results(self):
    #     qs = l_models.Result.objects.filter(owner_address=self._address)

    def get_all_rewards(self):
        qs = l_models.Result.objects.filter(owner_address=self._address)
        serializer = l_serializers.Result(qs, many=True)

        reward_field_list = ["reward_validators", "reward_validators_with_ssv",
                             "reward_all_operator", "reward_verified_operator"]

        show_key_list = ["validators", "ssv_amount"] + reward_field_list
        # show_key_map = {
        #     "validators"
        # }

        title_map = {
            "validators": "Validators",
            "ssv_amount": "SSV Holdings",
            "non_verified_operators": "Operators",
            "non_verified_operator_avg_performance": "Avg. Performance",
            "validators_managed_by_non_verified_operators": "Manged Validators",
            "_1": "Allocation Rewards",
            "reward_validators": "All validators alloc",
            "reward_validators_with_ssv": "Validators + SSV Holders alloc",
            "reward_all_operator": "All operators alloc",
            "reward_verified_operator": "Verified operators alloc",
        }

        show_data = []
        for key, value in title_map.items():
            show_data_item = {"title": value, "key": key}
            if key.startswith("_"):
                show_data.append(show_data_item)
                continue
            for res_data_item in serializer.data:
                show_data_item[res_data_item["round"]] = res_data_item[key]
                # show_data_item["round_total_reward"] = sum([res_data_item[key] for key in reward_field_list])
            show_data.append(show_data_item)

        round_reward_item = {"title": "Total (Round)"}
        total_reward = 0
        for res_data_item in serializer.data:
            round_reward = sum([res_data_item[key] for key in reward_field_list])
            round_reward_item[res_data_item["round"]] = round_reward
            total_reward += round_reward

        show_data.append(round_reward_item)
        # total_reward = sum(round_reward.values())
        show_data.append({"title": "Total (All Rounds)", "round1": total_reward})
        return show_data

        # [
        #     {"title": "validators", "round1": 32, "round2": 32},
        #     {"title": "rewad", "round1": 32},
        # ]
        # buf = {}
        # for result in serializer.data:
        #     round = result["round"]
        #     for key, value in result.items():
        #         if key not in buf.keys():
        #             buf[key] = {}
        #         buf[key][round] = value
        #
        # reward_list = []
        # for key, value in buf.items():
        #     value["title"] = key
        #     reward_list.append(value)
        #
        # return reward_list

    def get_round_rewards(self, round):
        pass
