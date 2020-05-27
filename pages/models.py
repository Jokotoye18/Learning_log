from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.email