from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ko'nikma nomi")
    percentage = models.IntegerField(verbose_name="Bilish darajasi (%)")
    
    def __str__(self):
        return f"{self.name} - {self.percentage}%"

    class Meta:
        verbose_name = "Ko'nikma"
        verbose_name_plural = "Ko'nikmalar"


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Loyiha nomi")
    description = models.TextField(verbose_name="Loyiha haqida qisqacha matn")
    technologies = models.CharField(max_length=200, verbose_name="Ishlatilgan texnologiyalar (vergul bilan ajrating)")
    link = models.URLField(blank=True, null=True, verbose_name="Loyiha havolasi (link)")
    image = models.ImageField(upload_to="projects/", blank=True, null=True, verbose_name="Loyiha rasmi")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"