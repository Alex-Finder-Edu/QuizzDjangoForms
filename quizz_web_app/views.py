from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Domain, Subdomain, Question, Quiz, CourseInfo, Course, CourseParagraph
from .forms import DomainForm, SubdomainForm, QuestionForm, QuizForm, CourseInfoForm, CourseForm, CourseParagraphForm


@login_required
def index(request):
    return render(request, "quizz_web_app/index.html", {
        "domain_count": Domain.objects.count(),
        "subdomain_count": Subdomain.objects.count(),
        "question_count": Question.objects.count(),
        "quiz_count": Quiz.objects.count(),
        "course_count": Course.objects.count(),
    })


# --- Domain ---

@login_required
def domain_list(request):
    domains = Domain.objects.prefetch_related("subdomains").all()
    return render(request, "quizz_web_app/domain_list.html", {"domains": domains})


@login_required
def domain_create(request):
    form = DomainForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("domain_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Add Domain"})


@login_required
def domain_update(request, pk):
    domain = get_object_or_404(Domain, pk=pk)
    form = DomainForm(request.POST or None, instance=domain)
    if form.is_valid():
        form.save()
        return redirect("domain_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Edit Domain"})


@login_required
def domain_delete(request, pk):
    domain = get_object_or_404(Domain, pk=pk)
    if request.method == "POST":
        domain.delete()
        return redirect("domain_list")
    return render(request, "quizz_web_app/confirm_delete.html", {"object": domain, "cancel_url": "domain_list"})


# --- Subdomain ---

@login_required
def subdomain_list(request):
    subdomains = Subdomain.objects.select_related("domain").all()
    return render(request, "quizz_web_app/subdomain_list.html", {"subdomains": subdomains})


@login_required
def subdomain_create(request):
    form = SubdomainForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("subdomain_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Add Subdomain"})


@login_required
def subdomain_update(request, pk):
    subdomain = get_object_or_404(Subdomain, pk=pk)
    form = SubdomainForm(request.POST or None, instance=subdomain)
    if form.is_valid():
        form.save()
        return redirect("subdomain_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Edit Subdomain"})


@login_required
def subdomain_delete(request, pk):
    subdomain = get_object_or_404(Subdomain, pk=pk)
    if request.method == "POST":
        subdomain.delete()
        return redirect("subdomain_list")
    return render(request, "quizz_web_app/confirm_delete.html", {"object": subdomain, "cancel_url": "subdomain_list"})


# --- Question ---

@login_required
def question_list(request):
    questions = Question.objects.select_related("subdomain__domain").all()
    return render(request, "quizz_web_app/question_list.html", {"questions": questions})


@login_required
def question_create(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("question_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Add Question"})


@login_required
def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    form = QuestionForm(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return redirect("question_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Edit Question"})


@login_required
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        question.delete()
        return redirect("question_list")
    return render(request, "quizz_web_app/confirm_delete.html", {"object": question, "cancel_url": "question_list"})


# --- Quiz ---

@login_required
def quiz_list(request):
    quizzes = Quiz.objects.prefetch_related("questions").all()
    return render(request, "quizz_web_app/quiz_list.html", {"quizzes": quizzes})


@login_required
def quiz_create(request):
    form = QuizForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("quiz_list")
    return render(request, "quizz_web_app/quiz_form.html", {"form": form, "title": "Create Quiz"})


@login_required
def quiz_update(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    form = QuizForm(request.POST or None, instance=quiz)
    if form.is_valid():
        form.save()
        return redirect("quiz_list")
    return render(request, "quizz_web_app/quiz_form.html", {"form": form, "title": "Edit Quiz"})


@login_required
def quiz_delete(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == "POST":
        quiz.delete()
        return redirect("quiz_list")
    return render(request, "quizz_web_app/confirm_delete.html", {"object": quiz, "cancel_url": "quiz_list"})


@login_required
def quiz_take(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.select_related("subdomain__domain").all()

    if request.method == "POST":
        results = []
        for question in questions:
            user_answer = request.POST.get(f"answer_{question.pk}", "").strip()
            is_correct = user_answer.lower() == question.correct_answer.strip().lower()
            results.append({
                "question": question,
                "user_answer": user_answer,
                "correct_answer": question.correct_answer,
                "is_correct": is_correct,
            })
        score = sum(1 for r in results if r["is_correct"])
        return render(request, "quizz_web_app/quiz_result.html", {
            "quiz": quiz,
            "results": results,
            "score": score,
            "total": len(results),
        })

    return render(request, "quizz_web_app/quiz_take.html", {"quiz": quiz, "questions": questions})


# --- CourseInfo ---

@login_required
def course_info_list(request):
    course_infos = CourseInfo.objects.all()
    return render(request, "quizz_web_app/course_info_list.html", {"course_infos": course_infos})


@login_required
def course_info_create(request):
    form = CourseInfoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("courseinfo_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Add Course Info"})


@login_required
def course_info_update(request, pk):
    course_info = get_object_or_404(CourseInfo, pk=pk)
    form = CourseInfoForm(request.POST or None, instance=course_info)
    if form.is_valid():
        form.save()
        return redirect("courseinfo_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Edit Course Info"})


@login_required
def course_info_delete(request, pk):
    course_info = get_object_or_404(CourseInfo, pk=pk)
    if request.method == "POST":
        course_info.delete()
        return redirect("courseinfo_list")
    return render(request, "quizz_web_app/confirm_delete.html", {"object": course_info, "cancel_url": "courseinfo_list"})


# --- Course ---

@login_required
def course_list(request):
    courses = Course.objects.select_related("domain", "subdomain", "course_info").all()
    return render(request, "quizz_web_app/course_list.html", {"courses": courses})


@login_required
def course_create(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("course_list")
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Add Course"})


@login_required
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect("course_detail", pk=pk)
    return render(request, "quizz_web_app/form.html", {"form": form, "title": "Edit Course"})


@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        return redirect("course_list")
    return render(request, "quizz_web_app/confirm_delete.html", {"object": course, "cancel_url": "course_list"})


@login_required
def course_detail(request, pk):
    course = get_object_or_404(
        Course.objects.select_related("domain", "subdomain", "course_info").prefetch_related("paragraphs"),
        pk=pk,
    )
    return render(request, "quizz_web_app/course_detail.html", {"course": course})


# --- CourseParagraph ---

@login_required
def paragraph_create(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    form = CourseParagraphForm(request.POST or None)
    if form.is_valid():
        paragraph = form.save(commit=False)
        paragraph.course = course
        paragraph.save()
        return redirect("course_detail", pk=course_pk)
    return render(request, "quizz_web_app/form.html", {"form": form, "title": f"Add Paragraph — {course}"})


@login_required
def paragraph_update(request, course_pk, pk):
    course = get_object_or_404(Course, pk=course_pk)
    paragraph = get_object_or_404(CourseParagraph, pk=pk, course=course)
    form = CourseParagraphForm(request.POST or None, instance=paragraph)
    if form.is_valid():
        form.save()
        return redirect("course_detail", pk=course_pk)
    return render(request, "quizz_web_app/form.html", {"form": form, "title": f"Edit Paragraph — {course}"})


@login_required
def paragraph_delete(request, course_pk, pk):
    course = get_object_or_404(Course, pk=course_pk)
    paragraph = get_object_or_404(CourseParagraph, pk=pk, course=course)
    if request.method == "POST":
        paragraph.delete()
        return redirect("course_detail", pk=course_pk)
    return render(request, "quizz_web_app/confirm_delete.html", {
        "object": paragraph,
        "cancel_href": reverse("course_detail", args=[course_pk]),
    })
