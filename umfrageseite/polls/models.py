from pyexpat import model
from django.db import models

class Poll(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.slug)

class Choice(models.Model):
    poll = models.ForeignKey(to='Poll', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0}: ({1})".format(self.poll.name, self.name)
