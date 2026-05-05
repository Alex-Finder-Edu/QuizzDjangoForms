from django.shortcuts import render, get_object_or_404, redirect
from .models import Domain, Subdomain, Question
from .forms import DomainForm, SubdomainForm, QuestionForm


def index(request):
    return render(request, "quizz_web_app/index.html", {
        "domain_count": Domain.objects.count(),
        "subdomain_count": Subdomain.objects.count(),
        "question_count": Question.objects.count(),
    })


# --- Domain ---

def domain_list(request):
    domains = Domain.objects.prefetch_related("subdomains").all()
    return render(request, "quizz_web_app/domain_list.html", {"domains": domains})


def domain_create(request):
    form = DomainForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("domain_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Add Domain"})


def domain_update(request, pk):
    domain = get_object_or_404(Domain, pk=pk)
    form = DomainForm(request.POST or None, instance=domain)
    if form.is_valid():
        form.save()
        return redirect("domain_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Edit Domain"})


def domain_delete(request, pk):
    domain = get_object_or_404(Domain, pk=pk)
    if request.method == "POST":
        domain.delete()
        return redirect("domain_list")
    return render(request, "quizz_web_app/confirm_delete.html", {"object": domain, "cancel_url": "domain_list"})


# --- Subdomain ---

def subdomain_list(request):
    subdomains = Subdomain.objects.select_related("domain").all()
    return render(request, "quizz_web_app/subdomain_list.html", {"subdomains": subdomains})


def subdomain_create(request):
    form = SubdomainForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("subdomain_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Add Subdomain"})


def subdomain_update(request, pk):
    subdomain = get_object_or_404(Subdomain, pk=pk)
    form = SubdomainForm(request.POST or None, instance=subdomain)
    if form.is_valid():
        form.save()
        return redirect("subdomain_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Edit Subdomain"})


def subdomain_delete(request, pk):
    subdomain = get_object_or_404(Subdomain, pk=pk)
    if request.method == "POST":
        subdomain.delete()
        return redirect("subdomain_list")
    return render(request, "quizz_web_app/confirm_delete.html", {"object": subdomain, "cancel_url": "subdomain_list"})


# --- Question ---

def question_list(request):
    questions = Question.objects.select_related("subdomain__domain").all()
    return render(request, "quizz_web_app/question_list.html", {"questions": questions})


def question_create(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("question_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Add Question"})


def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    form = QuestionForm(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return redirect("question_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Edit Question"})


def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        question.delete()
        return redirect("question_list")
    return render(request, "quizz_web_app/confirm_delete.html", {"object": question, "cancel_url": "question_list"})
