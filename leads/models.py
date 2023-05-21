from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    LOW = "faible"
    MEDIUM = "moyenne"
    HIGH = "forte"

    CHOICES_PRIORITY = (
        (LOW, "faible"),
        (MEDIUM, "moyenne"),
        (HIGH, "forte"),
    )

    NEW = 'nouveau'
    CONTACTED = 'contacté'
    WON = 'gagné'
    LOST = 'perdu'

    CHOICES_STATUS = (
        (NEW, 'nouveau'),
        (CONTACTED, 'contacté'),
        (WON, 'gagné'),
        (LOST, 'perdu'),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NEW)
    converted_to_client=models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
