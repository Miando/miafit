from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=3150)

    def __str__(self):
        return "%s (%s) - %s" % (self.subject, self.name, self.email)