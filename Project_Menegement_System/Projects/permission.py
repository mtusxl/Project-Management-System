from rest_framework import permissions

class ProjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(f"User: {request.user}, Author: {obj.author}, Method: {request.method}")

        if request.user == obj.author:
            return True

        if request.method in permissions.SAFE_METHODS:
            return request.user == obj.author or request.user in obj.members.all()
        return obj.author.username == request.user