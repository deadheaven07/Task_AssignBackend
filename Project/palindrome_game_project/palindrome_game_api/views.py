# palindrome_game_api/views.py
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .searializers import UserSerializer
from .models import User, Game

def index(request):
    return HttpResponse("Welcome to the Palindrome Game API!")

@api_view(['POST'])
def create_game(request):
    game = Game.objects.create(string='')
    return Response({'game_id': game.game_id}, status=status.HTTP_201_CREATED)
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_board(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response({'string': game.string}, status=status.HTTP_200_OK)
@api_view(['POST'])
def update_board(request, game_id, char):
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    game.append_char(char)
    if len(game.string) == 6:
        if game.is_palindrome():
            return Response({'message': 'Palindrome'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Not a Palindrome'}, status=status.HTTP_200_OK)
    return Response({'message': 'Character added'}, status=status.HTTP_200_OK)
@api_view(['GET'])
def list_games(request):
    games = Game.objects.all()
    game_ids = [game.game_id for game in games]
    return Response({'game_ids': game_ids}, status=status.HTTP_200_OK)