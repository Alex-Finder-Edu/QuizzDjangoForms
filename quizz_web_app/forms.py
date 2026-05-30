from django import forms
from .models import Domain, Subdomain, Question, Quiz


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


class QuizForm(forms.ModelForm):
    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.select_related("subdomain__domain").all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Quiz
        fields = ["title", "questions"]
