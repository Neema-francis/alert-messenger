from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

from app.constants import alert_color
from app.models import AlertNotification


class AlertCreateNotificationSerializer(ModelSerializer):

    class Meta():
        model = AlertNotification
        fields = ['user', 'alert_msg', 'alert_status', ]


class AlertListNotificationSerializer(ModelSerializer):

    alert_color = SerializerMethodField('get_alert_color')

    class Meta():
        model = AlertNotification
        fields = ['alert_msg', 'alert_status', 'alert_color', ]

    def get_alert_color(self, instance):
        return alert_color[instance.alert_status]