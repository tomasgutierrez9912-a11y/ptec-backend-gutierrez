from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from platforms.models import Platform
from .models import User, UserPlatform
from .serializers import LoginSerializer
from drf_yasg.utils import swagger_auto_schema


class LoginView(APIView):

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={200: "JWT tokens and platform name"},
        operation_description="Inicio de sesión usando email, password y plataforma."
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        platform_id = serializer.validated_data["platform"]

        try:
            platform = Platform.objects.get(id=platform_id)
        except Platform.DoesNotExist:
            return Response({"error": "Invalid platform"}, status=400)

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response({"error": "Invalid credentials"}, status=400)

        if not UserPlatform.objects.filter(user=user, platform=platform).exists():
            return Response(
                {"error": "User not registered in this platform"},
                status=403
            )

        refresh = RefreshToken.for_user(user)
        refresh["platform"] = platform.id  # JWT embed platform

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "platform": platform.name
        })