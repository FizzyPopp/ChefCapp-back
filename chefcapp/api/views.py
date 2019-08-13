from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .serializers import UserDetailSerializer


class AuthView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is None or not user.is_active:
            return Response({}, status=401)

        login(request, user)
        return Response({})

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


class UserDetailView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

