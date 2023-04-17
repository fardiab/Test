from rest_framework.response import Response
from users.serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status

from users.models import User

class RegisterView(APIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def get(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)