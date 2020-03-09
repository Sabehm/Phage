from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from evaluations.models import Evaluation
from registration.models import User

from evaluations.forms import EvaluationForm
from registration.forms import UserForm

# Create your views here.
class DashboardEvaluationList(LoginRequiredMixin, ListView):
    template_name   = "dashboard/evaluation_list.html"
    model           = Evaluation

    def get_queryset(self):
        queryset    = self.request.user.evaluation_set.all()
        return queryset

class DashboardEvaluationDetail(LoginRequiredMixin, DetailView):
    template_name   = "dashboard/dashboard.html"
    model           = Evaluation

class EvaluationCreateView(LoginRequiredMixin, CreateView):
    template_name   = "dashboard/create_evaluation.html"
    model           = Evaluation
    form_class      = EvaluationForm

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class UserCreateView(LoginRequiredMixin, CreateView):
    template_name   = "dashboard/create_user.html" 
    model           = User
    form_class      = UserForm

    def form_valid(self, form):
        return super().form_valid(form)