from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_volunteer = models.BooleanField(default=True)
    is_coordinator = models.BooleanField(default=False)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.title

class Registration(models.Model):
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    registered_at = models.DateTimeField(auto_now_add=True)
    attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ('volunteer', 'event') # Prevents double registration

    def __str__(self):
        return f"{self.volunteer.username} - {self.event.title}"