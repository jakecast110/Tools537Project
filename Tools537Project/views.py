from django.shortcuts import render

def showSurveys(request):
    return render(request, 'survey_dashboard.html')

def createSurvey(request):
    return render(request, 'create_survey.html')