from django.db import models

# Create your models here.
class Party(models.Model):
    name = models.CharField( max_length=150 )
    genre = models.CharField( max_length=100 )
    identifier = models.CharField( max_length=20 )
    type = models.CharField( max_length=10 )
    civil_status = models.CharField( max_length=20 )


class Customer(Party):
    family_responsibilities = models.IntegerField()
    type_customer = models.CharField( max_length=2 )
    residence_date = models.DateField()