from django.db import models


class Tasks(models.Model):
  _id= models.AutoField()
  title=models.CharField(max_length=100, null=True, blank=True)
  description=models.TextField(null=True,blank=True)
  completed=models.Boolean(default=False)
  created=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
      return self.title
    
    