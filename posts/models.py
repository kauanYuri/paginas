from django.db import models
from django.urls import reverse


class Post(models.Model):
    titulo = models.CharField(
        blank=True,
        null=True,
        max_length=200,
    )
    autor = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    texto = models.TextField()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):  # Insira no final do model
        return reverse('post_detail', args=[str(self.id)])
# Create your models here.
