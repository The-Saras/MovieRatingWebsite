from django.db import models

# Create your models here.
class Movie(models.Model):
    srno = models.AutoField(primary_key = True)
    MovName = models.CharField(max_length = 60)
    slug = models.CharField(max_length = 50)
    rating = models.FloatField()
    story = models.TextField()
    Movlanguage = models.CharField(max_length = 20)
    postImg = models.ImageField(upload_to="movie/images",default ="")
    catMov = models.TextField(max_length = 50)
    actors = models.TextField()
    trailerUrl = models.URLField()

    def __str__(self):
        return self.MovName