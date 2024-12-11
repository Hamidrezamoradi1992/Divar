from rest_framework.permissions import BasePermission


class SiteAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            user = request.user
            return bool(True if user.sait_admin else False)
        return bool(False)


class SuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            user = request.user
            return bool(True if user.is_superuser else False)
        return bool(False)
