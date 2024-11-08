from django.urls import path
from surveys import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns =[
    path('surveys/', views.SurveyList.as_view()),
    path('surveys/<int:pk>/', views.SurveyDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)