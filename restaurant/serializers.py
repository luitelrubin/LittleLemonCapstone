from datetime import datetime, timezone

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Menu, Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"

    def validate(self, data):
        price = data.get("price")
        if price is not None and price < 1:
            raise serializers.ValidationError("Price should be at least 1.00")

        inventory = data.get("inventory")
        if inventory is not None and inventory < 0:
            raise serializers.ValidationError(
                "Inventory should be greater than or equal to 0"
            )
        return data


class BookingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(write_only=True)
    model = serializers.CharField(write_only=True)

    class Meta:
        model = Booking
        fields = "__all__"

    def validate(self, data):
        no_of_guests = data.get("no_of_guests")
        if no_of_guests is not None and no_of_guests < 1:
            raise serializers.ValidationError("Guests should be at least one")
        booking_date = data["booking_date"]
        if booking_date is not None and booking_date < datetime.now(timezone.utc):
            raise serializers.ValidationError("New booking can't be made in the past")
        return data
