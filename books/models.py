from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256, null=True)
    shortDescription = models.CharField(max_length=256, null=True)
    longDespriction = models.TextField(null=True)

    def __str__(self):
        return f"{self.id} {self.title}"


