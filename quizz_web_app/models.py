from django.db import models


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
