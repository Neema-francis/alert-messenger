from django.db import models

from app.constants import STATUS

class AlertNotification(models.Model):
    """ Create model for alert message"""

    user = models.ForeignKey('auth.User', related_name='user_notification', on_delete=models.CASCADE)
    alert_msg = models.TextField(null=False, blank=False) # no need to create instance when alert message is empty
    created_by = models.DateTimeField(auto_now_add=True)
    alert_status = models.CharField(max_length=10, blank=False, default='info', choices=STATUS, )
    is_sent = models.BooleanField(default=False)