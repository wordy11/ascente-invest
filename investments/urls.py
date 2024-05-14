# urls.py
from django.urls import path
from.views import ListInvestmentsView, CreateInvestmentView

urlpatterns = [
    path('create', ListInvestmentsView.as_view(), name='list-investments'),
    path('list', CreateInvestmentView.as_view(), name='create-investment'),
    # Other paths...
]
