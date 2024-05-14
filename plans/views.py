from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Plans, Wallet, Transactions
from .serializers import PlansSerializer, WalletSerializer
from cryptapi import CryptAPIHelper
from dotenv import load_dotenv
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework.decorators import api_view, action
import os
import json

load_dotenv()

class PlansViewSet(viewsets.ModelViewSet):
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class TransferMoneyView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(name='amount', type=OpenApiTypes.STR, description='Amount to send', required=True),
        ],
        responses={200: OpenApiTypes.OBJECT},
    )
    def get(self, request, wallet_id, format=None):
        address = {
        'trc20/usdt': 'TSgcQFPgLy9wZH2HTp6Co59rXE4HG1cv4n',
        'eth': '0x1020103496a517c74B3Db4311D6FB242715b2bc4',
        'btc': 'bc1qkk3ur773wu4maen4ntjpkqhzlkphfsjh82c4qd',
        'trx': 'TSgcQFPgLy9wZH2HTp6Co59rXE4HG1cv4n',
        }

        try:
            wallet = Wallet.objects.get(uuid=wallet_id)
            user = wallet.user
        except Wallet.DoesNotExist:
            return Response({"error": "Wallet not found."}, status=404)

        amount_to_send = request.query_params.get('amount', 0)
        if float(amount_to_send) > 0:

            

            transaction = Transactions.objects.create(
                user=user,
                wallet=wallet,
                previous_balance=wallet.balance,
                present_balance=wallet.balance+float(amount_to_send),
                status='pending'
            )

            ca = CryptAPIHelper(wallet.token, address[wallet.token], os.getenv('CALLBACK'), {'transaction_id': transaction.uuid}, {})

            address = ca.get_address()['address_in']
            return Response({"address": address, "message": f"please make payment to {address}, to confirm ur transaction {transaction.uuid}"}, status=200)
        else:
            return Response({"error": "Amount to send must be greater than 0."}, status=400)
        

class CallbackView(APIView):
    def get(self, request, *args, **kwargs):
        # Assuming the payment gateway sends transaction details as query parameters
        cryptApiCallbackUUID = request.query_params.get('uuid', None)
        blockChainInTransactionHash = request.query_params.get('txid_in', None)
        blockChainOutTransactionHash = request.query_params.get('txid_out', None)
        internalTransactionID = request.query_params.get('transaction_id', None)

        try:
            transaction = Transactions.objects.get(uuid=internalTransactionID)
            wallet = transaction.wallet
        except Transactions.DoesNotExist:
            return Response({"error": "Transaction not found."}, status=404)
        except Wallet.DoesNotExist:
            return Response({"error": "Wallet not found."}, status=404)

        transaction.status = 'success'
        transaction.blockchain_in = blockChainInTransactionHash
        transaction.blockchain_out = blockChainOutTransactionHash
        transaction.crytp_api_uuid = cryptApiCallbackUUID
        transaction.save()

        wallet.balance = transaction.present_balance
        wallet.save()

        return Response({'message': '*ok*'}, status=200)

