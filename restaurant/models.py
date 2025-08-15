from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    class Meta:
        unique_together = (
            "name",
            "booking_date",
        )  # Booking limited to once for a day-time slot

    def __str__(self):
        return f"{self.name}'s booking"


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    class Meta:
        unique_together = ("title", "price")  # menu_item and price combination

    def __str__(self):
        return f"{self.title} : {str(self.price)}"
