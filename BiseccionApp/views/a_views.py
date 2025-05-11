from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from BiseccionApp.utils.calculations import biseccion
from BiseccionApp.serializers import BiseccionSerializer

class BiseccionAPI(APIView):
    def post(self, request):
        try:
            serializer = BiseccionSerializer(data=request.data)
            if serializer.is_valid():
                resultado = biseccion(serializer.validated_data)

                # Manejar el caso de error
                if "error" in resultado:
                    return Response({"error": resultado["error"]}, status=status.HTTP_400_BAD_REQUEST)

                # Extraer pasos y raíz
                pasos = resultado["pasos"]
                raiz = resultado["raiz"]

                return Response({"raiz": raiz, "pasos": pasos}, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)