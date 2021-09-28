from django.db import models


class File(models.Model):
    file = models.ImageField(upload_to='img', blank=False, null=False)

    def __str__(self):
        return self.file.name
