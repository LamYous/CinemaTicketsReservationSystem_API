from django.shortcuts import render, get_object_or_404
from .models import Hall, Movie, Showtime, Seat, Reservation
from .serializers import HallSerializer, MovieSerializer, SeatSerializer, ShowtimeSerializer, ReservationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Theater Views

@api_view(['GET','POST'])
def hall_list(request):
    if request.method == 'GET':
        halls = Hall.objects.all()
        serializer = HallSerializer(halls, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = HallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def hall_details(request, pk):
    try:
        hall = get_object_or_404(Hall, id=pk)
    except Hall.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = HallSerializer(hall, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = HallSerializer(hall, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        hall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Movie Views

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    try:
        movie = get_object_or_404(Movie, id=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Showtime Views
@api_view(['GET','POST'])
def showtim_list(request):
    if request.method == 'GET':
        showtims = Showtime.objects.all()
        serializer = ShowtimeSerializer(showtims, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ShowtimeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def showtime_details(request, pk):
    try:
        showtime = get_object_or_404(Showtime, id=pk)
    except Showtime.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ShowtimeSerializer(showtime, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ShowtimeSerializer(showtime, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        showtime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Reservation Views
@api_view(['GET', 'POST'])
def reservation_list(request):
    if request.method == 'GET':
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReservationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def reservation_details(request, pk):
    try:
        reservation = get_object_or_404(Reservation, id=pk)
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ReservationSerializer(reservation, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReservationSerializer(reservation, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Seat Views
@api_view(['GET', 'POST'])
def seat_list(request):
    if request.method == 'GET':
        seats = Seat.objects.all()
        serializer = SeatSerializer(seats, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SeatSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def seat_details(request, pk):
    try:
        seat = get_object_or_404(Seat, id=pk)
    except Seat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SeatSerializer(seat, data=request.data)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SeatSerializer(seat, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        seat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)