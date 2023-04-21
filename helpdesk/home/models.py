from django.db import models

# Create your models here.

class Client(models.Model):
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    admin_status = models.BooleanField(default=False)

    def __str__(self):
        return f'Client {self.firstname}-{self.lastname}'

class Message(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    messagely = models.TextField()

    def __repr__(self):
        return f'Message {self.client}'
