from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.core import serializers

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def reservations(request):
    date = request.GET.get("date", datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize("json", bookings)
    return render(request, "bookings.html", {"bookings": booking_json})


# Old implementation, please ignore
"""
class BookingView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            # Retrieve
            serialized_booking = BookingSerializer(get_object_or_404(Booking, id=pk))
            return Response(serialized_booking.data, status.HTTP_200_OK)
        else:
            # List
            bookings = Booking.objects.all()
            serialized_bookings = BookingSerializer(bookings, many=True)
            return Response(
                data=serialized_bookings.data, status=status.HTTP_200_OK
            )  # Return JSON

    def post(self, request):
        serialized_booking = BookingSerializer(data=request.data)
        if serialized_booking.is_valid():
            serialized_booking.save()
            return Response(
                {"message": "success", "data": serialized_booking.data},
                status=status.HTTP_201_CREATED,
            )
        return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)


class MenuView(APIView):
    def post(self, request):
        serialized_item = MenuSerializer(data=request.data)
        if serialized_item.is_valid():
            serialized_item.save()
            return Response(
                {"message": "success", "data": serialized_item.data},
                status=status.HTTP_201_CREATED,
            )
        return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is not None:
            # Retrieve
            serialized_item = MenuSerializer(get_object_or_404(Menu, id=pk))
            return Response(serialized_item.data, status=status.HTTP_200_OK)
        else:
            # List
            serialized_items = MenuSerializer(Menu.objects.all(), many=True)
            return Response(serialized_items.data, status=status.HTTP_200_OK)
"""
