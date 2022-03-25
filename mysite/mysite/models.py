import django.contrib.auth.models
from django.db import models


class Issues(models.Model):
    issue_id = models.IntegerField(primary_key=True)
    owner_id = models.IntegerField()
    public = models.IntegerField()
    tags = models.CharField(max_length=254)
    text = models.CharField(max_length=2000000)
    issue_name = models.CharField(max_length=254)
    urgency = models.IntegerField()
    status = models.IntegerField()
    time_spent = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'issues'
