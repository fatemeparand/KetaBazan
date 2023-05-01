from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    """
    Allows access only to superusers.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    """
     The request is is_staff as a user, or is a read-only request.
     """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_staff
        )


class IsAuthorOrReadOnly(BasePermission):
    """
     The request is Author, or is a read-only request.
     """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user.is_authenticated and
            # Get access to superuser
            request.user.is_superuser or
            # Get access to book author
            obj.owner == request.user
        )


class IsSuperUserOrStaffReadOnly(BasePermission):
    """
      The request is is_superuser as a user, or is_staff user can read-only
      """
    def has_permission(self, request, view):
        return bool(
            # Get access to is_staff user ReadOnly
            request.method in SAFE_METHODS and
            request.user and
            request.user.is_staff or
            # Get access to superuser full
            request.user and
            request.user.is_superuser
        )


