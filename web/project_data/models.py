from django.db import models


class Kickstarter(models.Model):
    name = models.CharField(max_length=1024)
    category = models.CharField(max_length=1024)
    main_category = models.CharField(max_length=1024)
    currency = models.CharField(max_length=1024)
    deadline = models.CharField(max_length=1024)
    goal = models.FloatField()
    launched = models.CharField(max_length=1024)
    pledged = models.FloatField()
    state = models.CharField(max_length=1024)
    backers = models.IntegerField()
    country = models.CharField(max_length=1024)
    usd_pledged_real = models.FloatField()
    usd_goal_real = models.FloatField()

    def __str__(self):
        return f'Name:  ({self.name}) | Category: {self.category} | Main Category: {self.main_category} | Currency: {self.currency} | Deadline: {self.deadline} | Goal: {self.goal} | Launched: {self.launched} | Pledged: {self.pledged} | State: {self.state} | Backers: {self.backers} | Country: {self.country}  | Real USD Pledged: {self.usd_pledged_real} | Real USD Goal: {self.usd_goal_real}'

    def __repr__(self):
        return f'Name:  ({self.name}) | Category: {self.category} | Main Category: {self.main_category} | Currency: {self.currency} | Deadline: {self.deadline} | Goal: {self.goal} | Launched: {self.launched} | Pledged: {self.pledged} | State: {self.state} | Backers: {self.backers} | Country: {self.country}  | Real USD Pledged: {self.usd_pledged_real} | Real USD Goal: {self.usd_goal_real}'
