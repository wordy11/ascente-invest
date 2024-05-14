from django.urls import path
from .views import ProfileListCreateView, ProfileRetrieveUpdateView

urlpatterns = [
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateView.as_view(), name='profile-retrieve-update'),
]
