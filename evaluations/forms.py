from django import forms
from .models import Evaluation

EVALUATION_CHOICES = [
    ("A", "Activa"),
    ("P", "En Pausa"),
    ("F", "Finalizada")
]

class EvaluationForm(forms.ModelForm):
    id_evaluation   = forms.CharField(
        max_length=100,
        help_text='ID de la Evaluación',
        widget=forms.TextInput(attrs={
            'class':'form-control'
        })
    )
    end_date        = forms.DateField(
        required=False,
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class':'form-control datetimepicker-input',
            'data-target':'#datetimepicker1'
        })
    )
    status          = forms.CharField(
        max_length=1,
        widget=forms.Select(
            choices=EVALUATION_CHOICES,
            attrs={
                'class':'form-control'
            }),
    )
    class Meta:
        model = Evaluation
        fields = ['id_evaluation', 'end_date', 'status']