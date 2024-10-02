from rest_framework import serializers
from . models import Hall, Movie, Seat, Showtime, Reservation

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class ShowtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showtime
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True)

    class Meta:
        model = Reservation
        fields = "__all__"

    def validate(self, data):
        selected_seats = data['seats']
        for seat in selected_seats:
            if not seat.is_available: # that the selected seats is not available
                raise serializers.ValidationError(f"Seat {seat.seat_number} is not available.")
        return data

    def create(self, validated_data):
        seats_data = validated_data.pop('seats')
        reservation = super().create(validated_data)
        for seat in seats_data:
            seat.is_available = False
            seat.save()
            reservation.seats.add(seat)
        return reservation
    