from rest_framework import viewsets, status, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet

from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ScanQRViewSet(ViewSet):
    http_method_names = ("post",)
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    @action(methods=("post",), detail=False)
    def search(self, *args, **kwargs):
        if 'base64_data' not in self.request.data:
            raise ValidationError({'base64_data': 'Scan your badge'})

        try:
            user = User.objects.get(qr_code=self.request.data['base64_data'])
        except User.DoesNotExist:
            raise ValidationError({'base64_data': 'Unauthorized! User not found'})

        # Serialize the user object
        serializer = UserSerializer(user)

        # Return the serialized user object in the response
        return Response({"detail": serializer.data}, status=status.HTTP_200_OK)
