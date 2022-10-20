from rest_framework.permissions import BasePermission

"""
    Personnalisation de  notre permission au endpoint de admin category
"""


class IsAdminAuthenticated(BasePermission):
    
    def has_permission(self, request, view):
        # Ne donnons l’accès qu’aux utilisateurs administrateurs authentifiés
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)
 
#   
class IsAdminStaffAuthenticated(BasePermission):
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)