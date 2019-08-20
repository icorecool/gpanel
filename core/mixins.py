# coding=utf-8
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView,
    DestroyAPIView, GenericAPIView,
)


class ReadOnlyModelViewSet(RetrieveModelMixin,
                           ListModelMixin,
                           GenericViewSet):
    """
    A viewset that provides default `list()` and `retrieve()` actions.
    """
    pass


class CreateReadModelViewSet(CreateModelMixin,
                             RetrieveModelMixin,
                             ListModelMixin,
                             GenericViewSet):
    """
    A viewset that provides default `create()`, `list()` and `retrieve()` actions.
    """
    pass


class UpdateReadModelViewSet(UpdateModelMixin,
                             RetrieveModelMixin,
                             ListModelMixin,
                             GenericViewSet):
    """
    A viewset that provides default `update()`, `list()` and `retrieve()` actions.
    """
    pass


class NoDestroyModelViewSet(CreateModelMixin,
                            RetrieveModelMixin,
                            UpdateModelMixin,
                            ListModelMixin,
                            GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()` and `list()` actions.
    """
    pass


class NoUpdateModelViewSet(CreateModelMixin,
                           RetrieveModelMixin,
                           DestroyModelMixin,
                           ListModelMixin,
                           GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `destroy()`,
    `partial_update()` and `list()` actions.
    """
    pass


class ModelViewSet(CreateModelMixin,
                   RetrieveModelMixin,
                   UpdateModelMixin,
                   DestroyModelMixin,
                   ListModelMixin,
                   GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass


class AllowPUTAsCreateMixin(object):
    """
    The following mixin class may be used in order to support PUT-as-create
    behavior for incoming requests.
    """

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object_or_none()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if instance is None:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        self.perform_update(serializer)
        return Response(serializer.data)

    def get_object_or_none(self):
        try:
            return self.get_object()
        except Http404:
            if self.request.method == 'PUT':
                # For PUT-as-create operation, we need to ensure that we have
                # relevant permissions, as if this was a POST request.  This
                # will either raise a PermissionDenied exception, or simply
                # return None.
                self.check_permissions(clone_request(self.request, 'POST'))
            else:
                # PATCH requests where the object does not exist should still
                # return a 404 response.
                raise
