from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hall(models.Model):
    name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=200)
    total_seats = models.IntegerField()

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    release_date = models.DateField()

    def __str__(self):
        return self.title
    
class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hall.name} - Seat {self.seat_number}"
    
class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    showtime = models.DateTimeField()
    reserved_seats = models.ManyToManyField(Seat, blank=True)

    def __str__(self):
        return f"{self.movie.title} at {self.showtime} in {self.hall.name}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat)
    reservation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation by {self.user.username} for {self.showtime.movie.title}"
    

