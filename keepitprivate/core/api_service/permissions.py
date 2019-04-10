from rest_framework.permissions import IsAuthenticated


class IsOwner(IsAuthenticated):
    """ Permission class used to check if an object is owned by the current Account """

    def has_object_permission(self, request, view, obj):
        """
        This method will check of the current `obj.owner_id` correspond to the
        current user's id
        """
        return obj.owner_id == request.user.id
