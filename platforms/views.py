from rest_framework.generics import ListAPIView
from .models import Platform
from .serializers import PlatformSerializer

class PlatformListView(ListAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer