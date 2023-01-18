from django.db import models

from utils.models import BaseModel

# Create your models here.


class Brand(BaseModel):
    """The class Brand is a model that has a name field that is a CharField
    with a max length of 100 this is going to be use as a foreign key in
    the product model

    Args:
        models (Model): the django models object.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(BaseModel):
    """The Product class is a model that has a sku, name,
    brand, and called field. The sku and name fields
    are character fields that have a max length of 20 and
    100 characters respectively. The brand field
    is a foreign key that relates the Product model to the
    Brand model. The called field is an integer
    field

    the called field is going to be use to know how many times the user has called the product.

    Args:
        models (Model): the django models object.
    """

    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    called = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.sku} {self.name}"
