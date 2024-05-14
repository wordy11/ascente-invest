from rest_framework import serializers
from.models import Plans, Wallet

class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'  # This will include all fields in the model


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'  # This will include all fields in the model