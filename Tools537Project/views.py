from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Tools537Project.models import Survey, Questions, Answers
from Tools537Project.serializers import SurveySerializer

@csrf_exempt
def survey_list(request):
    if request.method == 'GET':
        surveys = Survey.objects.all()
        serializer = SurveySerializer(surveys, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SurveySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def survey_detail(request, pk):
    try:
        survey = Survey.objects.get(pk=pk)
    except Survey.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SurveySerializer(survey)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SurveySerializer(survey, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        survey.delete()
        return HttpResponse(status=204)