from django.db import models


class BaseModel(models.Model):
    """This is used as a parent to add the fields status, creation_date, updated_date

    Args:
        models (Model): the django models object.
    """

    status = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True
