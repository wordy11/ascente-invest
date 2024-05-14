import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Plans(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=30, blank=False)
    duration = models.IntegerField(blank=False)
    rate = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Wallet(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    TOKEN_CHOICES = [
        ('btc', 'btc'),
        ('eth', 'eth'),
        ('usdt', 'trc20/usdt'),
        ('trx', 'trx'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0)
    token = models.CharField(
        max_length=10,
        choices=TOKEN_CHOICES,
        default='btc',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} wallet'


class Transactions(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    STATUS_CHOICES = [
        ('pending', 'PENDING'),
        ('failed', 'FAILED'),
        ('success', 'SUCCESS'),
    ]

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    wallet = models.ForeignKey(Wallet, on_delete=models.DO_NOTHING)
    previous_balance = models.FloatField(default=0.0)
    present_balance = models.FloatField(default=0.0)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )
    blockchain_in = models.CharField(max_length=255, blank=True)
    blockchain_out = models.CharField(max_length=255, blank=True)
    crytp_api_uuid = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.wallet.uuid} transaction'
