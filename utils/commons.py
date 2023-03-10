from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.views import Request, Response, status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import User
from users.permissions import IsAccountOwner


class CommonAppView(CreateAPIView):  # Views
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request: Request, *args, **kwargs) -> Response:
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {
                    "detail": "This user already has this type of information registered. Try to update it."
                },
                status.HTTP_409_CONFLICT,
            )
        except ValidationError as error:
            return Response({"detail": error.message}, error.code)


class CommonAppDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    
    def get_queryset(self):
        if not self.request.user:
            raise ValidationError("ERROOOOOU", 404)
        return self.queryset.filter(user_id=self.request.user)

    def get_object(self):
        return get_object_or_404(self.get_queryset(), user=self.request.user)

    def update(self, request: Request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as error:
            return Response({"detail": error.message}, error.code)


# ============================================
