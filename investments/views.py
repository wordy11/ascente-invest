# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InvestmentsSerializer
from .models import User, Wallet, Plans, Investments
import uuid

class CreateInvestmentView(APIView):
    def post(self, request, format=None):
        amount = request.data.get('amount')
        plan_id = request.data.get('plan')
        user = request.user
        # wallet_id = 
        serializer = InvestmentsSerializer(data=request.data)
        if serializer.is_valid():
            investment = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListInvestmentsView(APIView):
    def get(self, request, format=None):
        investments = Investments.objects.all()
        serializer = InvestmentsSerializer(investments, many=True)
        return Response(serializer.data)

