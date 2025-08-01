from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Character
from .serializers import CharacterSerializer


class CharacterList(APIView):
    def get(self, request):
        character = Character.objects.all()
        serializer = CharacterSerializer(character, many = True)
        return Response(serializer.data)


