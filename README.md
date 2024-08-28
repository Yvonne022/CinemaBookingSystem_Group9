## Django API Project
### Project Overview
This project is a Django-based REST API for managing movies, cinema halls, screenings, and bookings. It includes models, serializers, views, URL patterns, and tests to facilitate CRUD operations for each entity.

### 1. Description of the Models and Their Relationships
Models

Movie

Fields:
title (CharField): The title of the movie.
description (TextField): A brief description of the movie.
duration (IntegerField): The duration of the movie in minutes.
release_date (DateField): The release date of the movie.
Relationships: No direct relationships with other models.

CinemaHall

Fields:
name (CharField): The name of the cinema hall.
capacity (IntegerField): The maximum seating capacity of the cinema hall.
Relationships: No direct relationships with other models.
Screening

Fields:

movie (ForeignKey to Movie): The movie being screened.
hall (ForeignKey to CinemaHall): The cinema hall where the movie is screened.
start_time (DateTimeField): The start time of the screening.
Relationships: Links Movie and CinemaHall through foreign keys.
Booking

Fields:

screening (ForeignKey to Screening): The screening for which the booking is made.
customer_name (CharField): The name of the customer making the booking.
seats_reserved (IntegerField): The number of seats reserved.
booking_time (DateTimeField): The time when the booking was made (auto-filled).
Relationships: Links Screening through a foreign key.

Relationships Summary:

Movie and Screening: One-to-Many (One movie can have multiple screenings).

CinemaHall and Screening: One-to-Many (One cinema hall can have multiple screenings).

Screening and Booking: One-to-Many (One screening can have multiple bookings).

### 2. Explanation of the Views/Viewsets and Their Roles
ViewSets:

MovieViewSet: Handles CRUD operations for the Movie model.

CinemaHallViewSet: Manages CRUD operations for the CinemaHall model.

ScreeningViewSet: Manages CRUD operations for the Screening model.

BookingViewSet: Handles CRUD operations for the Booking model.

Roles:

MovieViewSet: Provides methods to list, create, retrieve, update, and delete movie records.

CinemaHallViewSet: Provides methods to list, create, retrieve, update, and delete cinema hall records.

ScreeningViewSet: Provides methods to list, create, retrieve, update, and delete screening records.

BookingViewSet: Provides methods to list, create, retrieve, update, and delete booking records.

### 3. Description of the Serializers and Any Validation Rules
Serializers:

MovieSerializer: Converts Movie model instances to JSON and vice versa.

CinemaHallSerializer: Converts CinemaHall model instances to JSON and vice versa.

ScreeningSerializer: Converts Screening model instances to JSON and vice versa.

BookingSerializer: Converts Booking model instances to JSON and vice versa.

Validation Rules:

MovieSerializer: Ensures that duration is a positive integer.

CinemaHallSerializer: No additional validation rules.

ScreeningSerializer: Ensures that the start_time is in the future relative to the current time.

BookingSerializer: Ensures that seats_reserved is a positive integer and that customer_name is not empty.

### 4. Overview of the URL Patterns and Their Purpose
URLs Configuration:

 List and Retrieve Endpoints:

URL Patterns: http://localhost:8000/api/movies/, http://localhost:8000/api/halls/, http://localhost:8000/api/screenings/, http://localhost:8000/api/bookings/

Purpose: Allows users to list all records or retrieve a specific record by its ID.

CRUD Operations:

POST: Create new records.

GET: Retrieve existing records.

PUT: Update existing records.

DELETE: Remove existing records.

Router Configuration:

DefaultRouter: Automatically generates the URL patterns for the API endpoints based on the registered viewsets.

### 5. Summary of the Tests Conducted

Testing Endpoints Using Postman:

POST Requests:

URL: http://localhost:8000/api/movies/

Purpose: Create new movie records.

Evidence: Screenshots of successful creation with JSON payloads.

![image](https://github.com/user-attachments/assets/29a02356-a08a-4fcc-ab32-bf6b2f155978)

![image](https://github.com/user-attachments/assets/49ef1e39-e260-4ee0-916b-daef9cf624b8)

![image](https://github.com/user-attachments/assets/d6092cc6-ea32-4806-b7d8-10f49cd93217)

![image](https://github.com/user-attachments/assets/831d12a2-0b10-4043-951e-aeae69cb69c6)


GET Requests:

URL: http://localhost:8000/api/movies/

Purpose: Retrieve the list of movies.

Evidence: Screenshots of successful retrieval showing the list of movies.

![image](https://github.com/user-attachments/assets/7790c81a-b3b7-4998-b0f0-a9fe9ccc31ef)


PUT Requests:

URL: http://localhost:8000/api/movies/<id>/

Purpose: Update movie records.

Evidence: Screenshots of successful updates with JSON payloads.

![image](https://github.com/user-attachments/assets/e248dd61-3b91-491d-9ccb-a860545dd0f5)



DELETE Requests:

URL: http://localhost:8000/api/movies/<id>/

Purpose: Delete specific movie records.

Evidence: Screenshots showing the 204 No Content status indicating successful deletion.


![image](https://github.com/user-attachments/assets/5cc6942a-5770-4336-a462-733480ecaec3)

