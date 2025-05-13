from rest_framework import permissions

class TasksPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.members.all()
        return request.user == obj.author