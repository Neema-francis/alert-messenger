import json
from django.shortcuts import (
    HttpResponse,
    render,
)
from rest_framework import (
    generics, 
    status,
)
from rest_framework.response import Response

from alert_messenger import settings
from app.models import AlertNotification
from app.serializers import (
    AlertCreateNotificationSerializer,
    AlertListNotificationSerializer,
)


def index(request):
    context = {}
    return render(request, "index.html", context=context)

def login_view(request):
    context = {}
    return render(request, "login.html", context=context)


class NotificationMessageCreateAPIView(generics.CreateAPIView):
    """
        Create notification message instance.
    """
    model = AlertNotification
    serializer_class = AlertCreateNotificationSerializer

    def post(self, request):
        if request.user.is_anonymous:
            return HttpResponse(json.dumps({"detail": "Not authorized"}), status=status.HTTP_401_UNAUTHORIZED)

        serializer_obj = self.get_serializer(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.create(serializer_obj.validated_data)
            return Response({"data":serializer_obj.data},status=status.HTTP_201_CREATED)

        return Response(
            {'data': serializer_obj.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )


class NotificationMessageListAPIView(generics.ListAPIView):
    """
        List notification message instances.
    """
    model = AlertNotification
    serializer_class = AlertListNotificationSerializer

    def get_queryset(self, ):
        queryset = AlertNotification.objects.filter(
            is_sent=False
        ).filter(
            user=self.request.user
        )[:settings.LIST_LIMIT]

        return queryset


    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return HttpResponse(
            json.dumps({"data": serializer.data}), 
            status=status.HTTP_200_OK
        )
