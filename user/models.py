
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class UtilisateurModel(AbstractUser):
    region = models.CharField(_('region'), max_length=100)
    ville = models.CharField(_('ville'), max_length=100)
    description = models.TextField(_('description'))
