from django.db import models

# Create your models here.
class Questions(models.Model):
    name = models.CharField(max_length=200)
    message=models.TextField(null=False)
    parent = models.BooleanField(null=False,default=False)
    child = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.PROTECT)

    def __str__(self):
        return self.name