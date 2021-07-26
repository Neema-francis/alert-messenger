from django.urls import path

from app import views

urlpatterns = [
    path('alert/create/', views.NotificationMessageCreateAPIView.as_view(), name='alert_create'), # create alert notification center
    path('alert/list/', views.NotificationMessageListAPIView.as_view(), name='alert_list'), # List our alert notification center
]
