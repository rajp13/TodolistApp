from django.db import models

# Create your models here.


# create a model 
class Task(models.Model):

    #display name instead of the self objects
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    storyPoints = models.PositiveIntegerField()
    action = models.TextField()


