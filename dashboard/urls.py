from django.urls import path
from .views import (
    DashboardEvaluationList,
    DashboardEvaluationDetail,
    EvaluationCreateView,
    UserCreateView,
)

urlpatterns = [
    path('', DashboardEvaluationList.as_view(), name="dashboard"),
    #path('<str:pk>/', DashboardEvaluationDetail.as_view(), name="evaluation"),
    path('create/evaluation', EvaluationCreateView.as_view(), name="create_evaluation"),
    path('create/user', UserCreateView.as_view(), name="create_User"),
]
