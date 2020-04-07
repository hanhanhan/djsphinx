from django.db import models
from djsphinx.users.models import User


class BallotItem(models.Model):
    choice = models.CharField(max_length=100)
    description = models.TextField()


class Vote(models.Model):
    """Record votes made"""
    date = models.DateField(auto_now_add=True)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    chosen = models.BooleanField()
    choice = models.ForeignKey(BallotItem, on_delete=models.CASCADE)

    def assign(self):
        """This is an example method"""
        return self.choice
