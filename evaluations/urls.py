from django.urls import path

from .views import api_detail_evaluation_view

app_name = 'getevals'

urlpatterns = [
    path('<slug>/', api_detail_evaluation_view, name="detail")
]
