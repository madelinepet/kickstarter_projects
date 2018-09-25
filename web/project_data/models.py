from django.db import models


# Create your models here.
class Kickstarter(models.Model):

    ID = models.CharField(max_length=1024)
    name = models.CharField(max_length=1024)
    category = models.CharField(max_length=1024)
    main_category = models.CharField(max_length=1024)
    currency = models.CharField(max_length=1024)
    deadline = models.DateTimeField(blank=True)
    goal = models.FloatField()
    launched = models.DateTimeField(blank=True)
    pledged = models.FloatField()
    state = models.CharField(max_length=1024)
    backers = models.IntegerField()
    country = models.CharField(max_length=1024)
    usd_pledged = models.FloatField()
    usd_pledged_real = models.FloatField()
    usd_goal_real = models.FloatField()

    def __str__(self):
        return '{}'.format(self.name)
