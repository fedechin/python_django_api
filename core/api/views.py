from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Joke
from api.serializers import JokeSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, parser_classes

@csrf_exempt
@swagger_auto_schema(
    method='GET',
    operation_summary="Get a random joke",
    responses={200: JokeSerializer()},
)
@swagger_auto_schema(
    method='POST',
    operation_summary="Create a new joke",
    request_body=JokeSerializer,
    responses={201: JokeSerializer(), 400: "Bad Request"},
)
@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def JokeViewSet(request):
    if request.method == 'GET':
        jokes = Joke.objects.order_by('?').first()
        serializer = JokeSerializer(jokes, many=False)
        return JsonResponse(serializer.data, safe=False)

    # method for creating the joke
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JokeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)