from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Device
from .serializers import DeviceSerializer
from users.models import UserPlatform


jwt_header = openapi.Parameter(
    'Authorization',
    openapi.IN_HEADER,
    description="Bearer <access_token>",
    type=openapi.TYPE_STRING,
    required=True
)


class DeviceListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[jwt_header],
        responses={200: DeviceSerializer(many=True)},
        operation_description="Lista los dispositivos del usuario autenticado para la plataforma especificada en el JWT."
    )
    def get(self, request):
        platform_id = request.auth.get("platform")
        user = request.user

        user_platform = UserPlatform.objects.filter(
            user=user,
            platform_id=platform_id
        ).first()

        if not user_platform:
            return Response({"detail": "UserPlatform not found"}, status=404)

        devices = Device.objects.filter(user_platform=user_platform)
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        manual_parameters=[jwt_header],
        request_body=DeviceSerializer,
        responses={201: DeviceSerializer()},
        operation_description="Crea un dispositivo vinculado al usuario autenticado y a la plataforma indicada en el JWT."
    )
    def post(self, request):
        platform_id = request.auth.get("platform")
        user = request.user

        user_platform = UserPlatform.objects.filter(
            user=user,
            platform_id=platform_id
        ).first()

        if not user_platform:
            return Response({"detail": "UserPlatform not found"}, status=404)

        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_platform=user_platform)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)