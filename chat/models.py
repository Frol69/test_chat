from django.db import models

class Message(models.Model):
    text = models.TextField()
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.text