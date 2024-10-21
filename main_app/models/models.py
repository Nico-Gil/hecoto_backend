from django.db import models

from hecoto_backend.users.models import (
    User
)


# Create your models here.
class Laboratories(models.Model):
    name = models.CharField(verbose_name=('Name'), max_length=45, help_text=('The name of the laboratorie.'))
    description = models.CharField(verbose_name=('Description'), max_length=255, help_text=('The description of the laboratorie'))
    create_user = models.ForeignKey(User, on_delete=models.CASCADE,help_text=('User Create Laboratorie')) 
    create_at = models.DateTimeField(verbose_name=('Create at'), auto_now_add=True)
    update_at = models.DateTimeField(verbose_name=('Update at'), auto_now=True, )

    def __str__(self):
        """Return laboratories's str representation."""
        return str(self.name)
