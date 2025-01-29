from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    """View для проверки работоспособности API."""

    permission_classes = [AllowAny]
    http_method_names = ["get"]

    @extend_schema(
        operation_id="health_check",
        description="Проверка работоспособности API",
        responses={
            status.HTTP_200_OK: {
                "type": "object",
                "properties": {"status": {"type": "string", "enum": ["ok"]}},
            }
        },
        tags=["healthcheck"],
    )
    def get(self, request, *args, **kwargs):  # noqa: ARG002
        """
        Возвращает статус работоспособности API.

        Returns:
            Response: JSON с полем status='ok'
        """
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
