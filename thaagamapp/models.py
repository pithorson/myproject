from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    subject = models.CharField(max_length=500)      

    def __str__(self):
        return self.first_name