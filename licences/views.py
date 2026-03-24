from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Licencia

class ValidateLicenceView(APIView):
    def get(self, request, uuid):
        try:
            licencia = Licencia.objects.get(id=uuid)
            hoy = date.today()
            is_active = hoy <= licencia.fecha_vencimiento
            return Response({"active": is_active}, status=status.HTTP_200_OK)
        except (Licencia.DoesNotExist, ValueError):
            return Response({"active": False}, status=status.HTTP_200_OK)
