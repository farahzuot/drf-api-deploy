from rest_framework import permissions

class PemissionsClass(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        #read only
        if request.user.id == 1:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'DELETE' and request.user.id != 1:
            return False

        if obj.author == request.user:
            return True

