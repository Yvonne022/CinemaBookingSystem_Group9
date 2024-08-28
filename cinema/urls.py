from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, CinemaHallViewSet, ScreeningViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'halls', CinemaHallViewSet)
router.register(r'screenings', ScreeningViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
