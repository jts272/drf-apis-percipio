from django.shortcuts import get_object_or_404, render

# For issuing error status codes
from rest_framework import status

# Our view returns an HTTP response as a rest framework response object
from rest_framework.response import Response

# Allows us to define multiple HTTP methods corresponding to a view class
# E.g. a single view to cater to GET, POST and so on
from rest_framework.views import APIView

from .models import Actor
from .serializers import ActorSerializer


# Create your views here.
class ActorList(APIView):
    """Inherits from API view to process HTTP request methods."""

    def get(self, request):
        # Get all `Actor` instances
        actors = Actor.objects.all()
        # Construct a response object from the retrieved instances
        # `many` is set as it is representing more than one actor
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Accept the data sent in the request object and serialize it
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            # Entry is saved in the database
            serializer.save()
            # Include the data passed in the response and specify status code
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Likewise error data is shown with a specific status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorByID(APIView):
    """Inherits from the APIView to handle multiple types of HTTP requests.

    Requires two methods to be defined to GET the instance in question.
    """

    def get_object(self, pk):
        # Callback function to get the actor in question from the request
        return Actor.objects.get(pk=pk)

    def get(self, request, pk):
        # actor = self.get_object(pk)
        # My refactor makes the `get_object` method unnecessary
        actor = get_object_or_404(Actor, pk=pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    def put(self, request, pk):
        # Get the particular resource in question
        actor = get_object_or_404(Actor, pk=pk)
        # Serialize the object with the `PUT` data
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Just get the object
        actor = get_object_or_404(Actor, pk=pk)
        # Delete it
        actor.delete()
        # No serializer required as we are not sending any data back
        # Return an OK response, with no data being found at that endpoint now
        return Response(status=status.HTTP_204_NO_CONTENT)
