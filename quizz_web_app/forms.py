from django import forms
from .models import Domain, Subdomain, Question


class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = ["name"]


class SubdomainForm(forms.ModelForm):
    class Meta:
        model = Subdomain
        fields = ["name", "domain"]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["text", "correct_answer", "subdomain"]
