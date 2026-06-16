from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # Domain
    path("domains/", views.domain_list, name="domain_list"),
    path("domains/add/", views.domain_create, name="domain_create"),
    path("domains/<int:pk>/edit/", views.domain_update, name="domain_update"),
    path("domains/<int:pk>/delete/", views.domain_delete, name="domain_delete"),

    # Subdomain
    path("subdomains/", views.subdomain_list, name="subdomain_list"),
    path("subdomains/add/", views.subdomain_create, name="subdomain_create"),
    path("subdomains/<int:pk>/edit/", views.subdomain_update, name="subdomain_update"),
    path("subdomains/<int:pk>/delete/", views.subdomain_delete, name="subdomain_delete"),

    # Question
    path("questions/", views.question_list, name="question_list"),
    path("questions/add/", views.question_create, name="question_create"),
    path("questions/<int:pk>/edit/", views.question_update, name="question_update"),
    path("questions/<int:pk>/delete/", views.question_delete, name="question_delete"),

    # Quiz
    path("quizzes/", views.quiz_list, name="quiz_list"),
    path("quizzes/add/", views.quiz_create, name="quiz_create"),
    path("quizzes/<int:pk>/edit/", views.quiz_update, name="quiz_update"),
    path("quizzes/<int:pk>/delete/", views.quiz_delete, name="quiz_delete"),
    path("quizzes/<int:pk>/take/", views.quiz_take, name="quiz_take"),

    # CourseInfo
    path("course-info/", views.course_info_list, name="courseinfo_list"),
    path("course-info/add/", views.course_info_create, name="courseinfo_create"),
    path("course-info/<int:pk>/edit/", views.course_info_update, name="courseinfo_update"),
    path("course-info/<int:pk>/delete/", views.course_info_delete, name="courseinfo_delete"),

    # Course
    path("courses/", views.course_list, name="course_list"),
    path("courses/add/", views.course_create, name="course_create"),
    path("courses/<int:pk>/", views.course_detail, name="course_detail"),
    path("courses/<int:pk>/edit/", views.course_update, name="course_update"),
    path("courses/<int:pk>/delete/", views.course_delete, name="course_delete"),

    # CourseParagraph
    path("courses/<int:course_pk>/paragraphs/add/", views.paragraph_create, name="paragraph_create"),
    path("courses/<int:course_pk>/paragraphs/<int:pk>/edit/", views.paragraph_update, name="paragraph_update"),
    path("courses/<int:course_pk>/paragraphs/<int:pk>/delete/", views.paragraph_delete, name="paragraph_delete"),
]
