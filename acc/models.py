from django.db import models

# Create your models here.

# Create your models here.
class customer(models.Model):

   name = models.CharField(max_length = 20)
   mail = models.CharField(max_length = 50)
   course = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()
   branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True,default = 1)

   def __str__(self):   # What to be displayed when Dreamreal.objects.all() is called
       return self.name+''
   class Meta:
      db_table = "Account details"

class Branch(models.Model):
   branchName = models.CharField(max_length = 30)
   accnumber = models.IntegerField()