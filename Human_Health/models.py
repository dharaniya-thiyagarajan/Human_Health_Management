from django.db import models

# Create your models here.
class sleep(models.Model):
    Date = models.DateField()
    StartTime = models.TimeField()
    EndTime = models.TimeField()

    class Meta:
        db_table = "sleep"
        
    def __str__(self):
     return f"{self.Date}-{self.StartTime}-{self.EndTime}"