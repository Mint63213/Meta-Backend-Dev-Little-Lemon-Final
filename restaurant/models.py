from django.db import models
import datetime



class Booking(models.Model):
   first_name = models.CharField(max_length=50)    
   last_name = models.CharField(max_length=50)
   guest_number = models.SmallIntegerField()
   comment = models.CharField(max_length=1000)
   date = models.DateField(default=datetime.date.today, blank=False)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


class Menu(models.Model):
   name = models.CharField(max_length=50)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   menu_item_description = models.TextField(max_length=1000)

   def __str__(self):
      return self.name