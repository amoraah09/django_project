from django.shortcuts import render, redirect, get_object_or_404
from .models import TouristSpots
from django.views.decorators.csrf import csrf_exempt

def index(request):
    # this view returns index
    return render(request, 'touristSpotModule/index.html')

def spots(request):
    return render(request, 'touristSpotModule/spotList.html', {'spots': __getSpots()})

def register(request):
    return render(request, 'touristSpotModule/register.html')

def spot(request, sId):
    spot = get_object_or_404(TouristSpots, pk=sId)
    context = {'spot': spot}
    return render(request, 'touristSpotModule/spot.html', context)

def __getSpots():
    spots = TouristSpots.objects.order_by('name')
    return spots

@csrf_exempt
def filterSpots(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        searchByName = request.POST.get('optionName')
        searchByCity = request.POST.get('optionCity')

        if searchByName and searchByCity:
            spots = TouristSpots.objects.filter(
                name__icontains=keyword
            ) | TouristSpots.objects.filter(
                city__icontains=keyword
            )
        elif searchByName:
            spots = TouristSpots.objects.filter(name__icontains=keyword)
        elif searchByCity:
            spots = TouristSpots.objects.filter(city__icontains=keyword)
        else:
            spots = __getSpots()
            
        return render(request, 'touristSpotModule/spotList.html', {'spots': spots})
    else:
        return render(request, 'touristSpotModule/search.html')

@csrf_exempt
def add_spot(request):
    if request.method == "POST":
        name = request.POST['name']
        city = request.POST['city']
        description = request.POST['description']
        location = request.POST['location']

        new_spot = TouristSpots(name=name, city=city, description=description, location=location)
        new_spot.save()

        return redirect('spots')

    return render(request, 'touristSpotModule/add_spot.html')

@csrf_exempt
def edit_spot(request, sId):
    spot = get_object_or_404(TouristSpots, pk=sId)

    if request.method == "POST":
        spot.name = request.POST['name']
        spot.city = request.POST['city']
        spot.description = request.POST['description']
        spot.location = request.POST['location']
        spot.save()

        return redirect('spots')

    context = {'spot': spot}
    return render(request, 'touristSpotModule/edit_spot.html', context)
