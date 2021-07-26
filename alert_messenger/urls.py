from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView

from app import views
from alert_messenger import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # for authenticating
    path('', views.index),
    path('login', views.login_view),
    path('api/', include('app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
