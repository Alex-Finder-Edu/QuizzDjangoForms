from django.db import models
from django.utils import timezone


class Domain(models.Model):
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name


class Subdomain(models.Model):
    name = models.CharField(max_length=100)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name="subdomains")

    class Meta:
        unique_together = ("name", "domain")

    def __str__(self):
        return f"{self.domain} — {self.name}"


class Question(models.Model):
    text = models.TextField()
    correct_answer = models.TextField()
    subdomain = models.ForeignKey(Subdomain, on_delete=models.CASCADE, related_name="questions")

    def __str__(self):
        return self.text[:80]


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    questions = models.ManyToManyField(Question, related_name="quizzes", blank=True)

    def __str__(self):
        return self.title


class CourseInfo(models.Model):
    title = models.CharField(max_length=200)
    platform_name = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name="courses")
    subdomain = models.ForeignKey(Subdomain, on_delete=models.CASCADE, related_name="courses")
    url = models.URLField(null=True, blank=True)
    course_info = models.ForeignKey(
        CourseInfo, on_delete=models.SET_NULL, null=True, blank=True, related_name="courses"
    )
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class CourseParagraph(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="paragraphs")
    paragraph_index = models.PositiveIntegerField()
    paragraph_text = models.TextField()

    class Meta:
        ordering = ["paragraph_index"]
        unique_together = ("course", "paragraph_index")

    def __str__(self):
        return f"{self.course} — §{self.paragraph_index}"
