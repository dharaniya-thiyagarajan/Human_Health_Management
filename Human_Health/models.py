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






class Sleep(models.Model):
       Date=models.DateField()
       StartTime=models.TimeField()
       EndTime=models.TimeField()


class Meta:
      db_table= "Sleep" 

def __str__(self):
      return f"{self.Date}-{self.StartTime}-{self.EndTime}"   






class Water(models.Model):
       Date=models.DateField()
       Quantity=models.PositiveIntegerField()


class Meta:
      db_table= "Water" 

def __str__(self):
      return f"{self.Date}-{self.Quantity}" 



class Walk(models.Model):
       Date=models.DateField()
       Distance=models.PositiveIntegerField()


class Meta:
      db_table= "Walk" 

def __str__(self):
      return f"{self.Date}-{self.Distance}"  



class Mobile(models.Model):
       Date=models.DateField()
       Hour=models.PositiveIntegerField()
       Minute=models.PositiveIntegerField()


class Meta:
      db_table= "Mobile" 

def __str__(self):
      return f"{self.Date}-{self.Hour}-{self.Minute}"
  

class Location(models.Model):
       Name=models.CharField(max_length=30)
       

class Meta:
      db_table= "Location" 

def __str__(self):
      return f"{self.Name}"
  