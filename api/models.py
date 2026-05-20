from django.db import models


class Item(models.Model):
    CATEGORY_LOST = 'lost'
    CATEGORY_FOUND = 'found'
    CATEGORY_CHOICES = [
        (CATEGORY_LOST, 'Lost'),
        (CATEGORY_FOUND, 'Found'),
    ]

    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    contact = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.title} ({self.category})"
