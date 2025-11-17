from rest_framework.permissions import BasePermission

class IsPlatformUser(BasePermission):
    def has_permission(self, request, view):
        platform_id_in_token = request.user.token.get("platform_id")
        return platform_id_in_token is not None