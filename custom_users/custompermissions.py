from rest_framework.permissions import BasePermission


class BlockUser(BasePermission):
    """
    Permission class to check whether user is blocked or not
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_blocked != True)

