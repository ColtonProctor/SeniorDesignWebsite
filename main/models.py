from django.db import models

class Property(models.Model):
   state = models.CharField(max_length=5, default = "none")
   recorded = models.CharField(max_length=15, default = "none")
   date = models.CharField(max_length=10, default = "none")
   grantor = models.CharField(max_length=50, default = "none")
   address = models.CharField(max_length=50, default = "none")
   city = models.CharField(max_length=30, default = "none")
   grantee = models.CharField(max_length=50, default = "none")
   price = models.IntegerField(default = 0, null = True)
   propType = models.CharField(max_length=3, default = "none")
   built = models.CharField(max_length=5, default = "none")
   acreage = models.FloatField(default = 0.0, null = True)
   impsq = models.FloatField(default = 0.0, null = True)
   units = models.FloatField(default = 0.0, null = True)
   landsq = models.FloatField(default = 0.0, null = True)
   sfimp = models.CharField(max_length=10, default = "none")
   unitimp = models.CharField(max_length=10, default = "none")
   sfland = models.CharField(max_length=10, default = "none")
   garage = models.FloatField(default = 0.0, null = True)
   caprate = models.FloatField(default = 0.0, null = True)
   noi = models.FloatField(default = 0.0, null = True)
   exp = models.FloatField(default = 0.0, null = True)
   egi = models.FloatField(default = 0.0, null = True)
   occup = models.FloatField(default = 0.0, null = True)
   corner = models.CharField(max_length=5, default = "none")
   regshape = models.CharField(max_length=10, default = "none")
   utilities = models.CharField(max_length=20, default = "none")
   location = models.FloatField(default = 0.0, null = True)
   quality = models.FloatField(default = 0.0, null = True)
   condition = models.FloatField(default = 0.0, null = True)
   description = models.CharField(max_length=50, default = "none")
   comments = models.CharField(max_length=50, default = "none")
   
   def __str__(self):
      return self.propType + "  " + self.address + "  " + self.city


