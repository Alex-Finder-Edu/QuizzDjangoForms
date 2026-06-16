from django import forms
from .models import Domain, Subdomain, Question, Quiz, CourseInfo, Course, CourseParagraph


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


class CourseInfoForm(forms.ModelForm):
    class Meta:
        model = CourseInfo
        fields = ["title", "platform_name", "url"]


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "domain", "subdomain", "url", "course_info", "date_created"]
        widgets = {
            "date_created": forms.DateInput(attrs={"type": "date"}),
        }


class CourseParagraphForm(forms.ModelForm):
    class Meta:
        model = CourseParagraph
        fields = ["paragraph_index", "paragraph_text"]
