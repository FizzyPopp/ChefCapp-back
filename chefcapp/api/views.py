from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .serializers import RecipeDetailSerializer
from items.models import Recipe


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


class RecipeListView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer
