from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Evaluation
from .serializers import EvaluationSerializer

# Create your views here.
@api_view(['GET', ])
def api_detail_evaluation_view(request, slug):
    pass
    '''try:
        evaluation = Evaluation.objects.get(slug=slug)
    except Evaluation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = EvaluationSerializer(evaluation)
        return Response(serializer.data)'''
