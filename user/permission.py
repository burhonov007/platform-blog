from rest_framework.permissions import BasePermission


class IsModeratorUser(BasePermission):
    """
    Allows access only to moderator users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_moderator)