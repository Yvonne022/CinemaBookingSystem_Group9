from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in minutes")
    release_date = models.DateField()

class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

class Booking(models.Model):
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    seats_reserved = models.IntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)

class Review(models.Model):  
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()  
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)