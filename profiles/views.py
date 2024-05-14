from rest_framework import generics
from.models import Profile
from.serializers import ProfileSerializer, ProfileReadSerializer

class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ProfileSerializer
        return ProfileReadSerializer
