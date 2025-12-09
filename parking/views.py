from django.shortcuts import render, get_object_or_404
from .models import Floor, ParkingSpot


def dashboard(request):
    floors = Floor.objects.all()
    spots = ParkingSpot.objects.all()
    return render(request, 'parking/dashboard.html', {
        'floors': floors,
        'spots': spots
    })
def floor_detail(request, name):
    floor = get_object_or_404(Floor, name=name)

    
    spots = ParkingSpot.objects.filter(sector__floor=floor)

    context = {
        'floor': floor,
        'spots': spots,
        'total': spots.count(),
        'occupied': spots.filter(is_occupied=True).count(),
        'available': spots.filter(is_occupied=False).count(),
        'available_spots': spots.filter(is_occupied=False),
    }

    return render(request, 'parking/floor_detail.html', context)
