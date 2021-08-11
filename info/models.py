from django.db import models

# Create your models here.


class cv(models.Model):
    cv= models.FileField(upload_to='cv/')
    time=models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    company= models.CharField(max_length=255)
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.company+ ' - ' + self.message