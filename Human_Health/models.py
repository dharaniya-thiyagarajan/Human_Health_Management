from django.db import models


class Food(models.Model):
    Date=models.DateField()
    Breakfasttime=models.TimeField()
    BreakfastLocation=models.CharField(max_length=30)
    LunchTime= models.DateField()
    LunchLocation=models.CharField(max_length=30)
    DinnerTime=models.TimeField()
    DinnerLocation=models.CharField(max_length=30)

class Meta:
        db_table="Food"

def __str__ (self):
    return f"{self.Date}-{self.Breakfasttime}-{self.BreakfastLocation}-{self.LunchTime}-{self.LunchLocation}-{self.DinnerTime}-{self.DinnerLocation}"