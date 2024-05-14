from django.db import models
import uuid
from django.contrib.auth.models import User
from plans.models import Wallet
from plans.models import Plans

# Create your models here.

class Investments(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    amount = models.FloatField()
    expected_return = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    wallet = models.ForeignKey(Wallet, on_delete=models.DO_NOTHING)
    plan = models.ForeignKey(Plans, on_delete=models.DO_NOTHING)
    invested_date = models.DateField(null=True)
    expected_date = models.DateField(null=True)
    last_viewed = models.DateField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} investment'