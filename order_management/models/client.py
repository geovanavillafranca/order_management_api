from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100, blank=False, )
    phone_number = models.CharField(max_length=11, blank=False, )
    description = models.TextField()
    email = models.EmailField()
    company_name = models.CharField(max_length=120)

    address = models.CharField(max_length=150)
    address_number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    zone = models.CharField(max_length=100, blank=False)

    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.company_name
