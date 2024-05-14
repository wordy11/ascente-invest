# serializers.py
from rest_framework import serializers
from .models import Investments, User, Wallet, Plans

class InvestmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investments
        fields = '__all__'


