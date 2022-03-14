from django.db import models

# Create your models here.


class Result(models.Model):
    round = models.CharField(max_length=10, db_index=True)
    owner_address = models.CharField(max_length=50)
    verified_operators = models.IntegerField()
    verified_operators_av_performance = models.FloatField()
    validators_managed_by_verified_operators = models.IntegerField()
    non_verified_operators = models.IntegerField()
    non_verified_operator_avg_performance = models.FloatField()
    validators_managed_by_non_verified_operators = models.IntegerField()
    validators = models.IntegerField()
    ssv_amount = models.FloatField()
    reward_validators = models.FloatField()
    reward_validators_with_ssv = models.FloatField()
    reward_verified_operator = models.FloatField()
    reward_all_operator = models.FloatField()
    total_rewards = models.FloatField()

    class Meta:
        unique_together = (("owner_address", "round"), )


class DepositKey(models.Model):
    hex = models.TextField()
    dir_name = models.CharField(max_length=100, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)


