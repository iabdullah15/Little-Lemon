from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.

def index(request):

    # return HttpResponse('Hello')
    return render(request, 'index.html')

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]