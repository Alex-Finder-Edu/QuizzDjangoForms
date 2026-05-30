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
]
