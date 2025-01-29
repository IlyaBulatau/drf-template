from django.urls import path

from core.views import HealthCheckView


urlpatterns = [
    path("healthcheck", HealthCheckView.as_view()),
]
