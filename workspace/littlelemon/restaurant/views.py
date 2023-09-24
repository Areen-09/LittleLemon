from django.shortcuts import render
from .models import Menu, Booking
from django.contrib.auth.models import User
import rest_framework
from rest_framework import permissions, viewsets
from rest_framework import generics
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
# Create your views here.
def index(request):
     return render(request, 'index.html', {})
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
class BookingViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]