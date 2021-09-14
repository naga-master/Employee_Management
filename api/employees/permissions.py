from rest_framework import permissions
from typing import Type

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Description: Check if request has Authenticated
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user # return true if user is authenticated