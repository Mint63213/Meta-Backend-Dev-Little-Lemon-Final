from rest_framework.permissions import BasePermission

class IsAuthenticatedAndStaff(BasePermission):
    """
    Custom permission to only allow authenticated users who are staff.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a staff member
        return request.user and request.user.is_authenticated and request.user.is_staff