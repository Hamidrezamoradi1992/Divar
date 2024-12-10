from rest_framework.permissions import BasePermission


class SiteAdmin(BasePermission):
    def has_permission(self, request, view):
        print('superuser', request.user)
        if request.user and request.user.is_authenticated:
            user = request.user
            print('sait_admin',user.sait_admin)
            return bool(True if user.sait_admin else False)
        return bool(False)


class SuperUser(BasePermission):
    def has_permission(self, request, view):
        print('superuser',request.user)
        if request.user and request.user.is_authenticated:
            user = request.user
            print('is_superuser',user.is_superuser)
            return bool(True if user.is_superuser else False)
        return bool(False)
