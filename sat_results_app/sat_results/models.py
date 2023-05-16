from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    sat_score = models.FloatField()
    
    @property
    def passed(self):
        return "Pass" if self.sat_score > 30 else "Fail"
