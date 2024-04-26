from django.urls import path

from .views import WhatsAppAPIView

urlpatterns = [
    path("welcome/", WhatsAppAPIView.as_view(), name="send_message"),
]
