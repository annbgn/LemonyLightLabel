from django.db import models


class Item(models.Model):
    type = models.CharField(
        max_length=20
    )  # TODO think of choices. the only option now is earrings so this field is not informative
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    price_currency = models.CharField(
        max_length=3
    )  # TODO choices or make a model for price and its currency
    picture = models.ImageField(
        blank=True, null=True, upload_to="item_images"
    )  # todo ponder upon a case of several images per item. should it be an array of image fields or array of foreignkeys to a different model which represents a photo and info about it?

    def __repr__(self):
        return "<%s: %i %s>" % (self.__class__.__name__, self.id, self.name)