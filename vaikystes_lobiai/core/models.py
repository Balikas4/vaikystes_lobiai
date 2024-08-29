from django.db import models

class Email(models.Model):
    name = models.CharField(max_length=100, db_index = True)
    email = models.EmailField(unique=True)
    message = models.TextField(blank=True, max_length = 100000)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    