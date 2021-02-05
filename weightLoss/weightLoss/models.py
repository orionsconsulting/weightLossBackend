from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)


class WeightTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(decimal_places=2, max_digits=5)

    class Meta:
        ordering = ('date'),