from django.shortcuts import render

def showSurveys(request):
    return render(request, 'survey_dashboard.html')