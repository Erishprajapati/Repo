# from rest_framework import permissions

# class IsAdminOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user and request.user.is_authenticated:
#             if request.user.is_superuser:
#                 return True
#             if request.method in permissions.SAFE_METHODS:
#                 return True
#             return False
        
