from django.urls import path, include
from rest_framework.routers import DefaultRouter
from.views import PlansViewSet, WalletViewSet, TransferMoneyView, CallbackView

router = DefaultRouter()
router.register(r'plans', PlansViewSet)
router.register(r'wallets', WalletViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('transfer-money/<uuid:wallet_id>/', TransferMoneyView.as_view(), name='transfer-money'),
    path("callback/", CallbackView.as_view(), name="callback"),
]
