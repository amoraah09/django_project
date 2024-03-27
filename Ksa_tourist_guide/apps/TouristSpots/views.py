from django.shortcuts import render, redirect
from .models import ToutistSpots

def index(request):
    # this view returns index
    return render(request, 'touristSpotModule/index.html')

def spots(request):
    return render(request, 'touristSpotModule/spotList.html', {'spots':__getSpots()})
def register(request):
    return render(request, 'touristSpotModule/register.html')

def spot(request, sId):
    
    spot1 = {'id':12344321, 'name':'Al Khobar', 'description':'A vibrant city in the Eastern Province of KSA'}
    spot2 = {'id':56788765, 'name':'Najran', 'description':'A city rich with history in the southern region of KSA'}
    
    targetSpot = None
    if spot1['id'] == sId: targetSpot = spot1
    if spot2['id'] == sId: targetSpot = spot2
    
    if targetSpot == None: return redirect('/spots')
    
    context = {'spot':targetSpot} # spot is the variable name accessible by template
    return render(request, 'TouristSpotModule/spot.html', context)

def __getSpots():
    spots = ToutistSpots.objects.order_by('name')
    return spots;

def filterSpots(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        searchByName = request.POST.get('optionName') == 'on'
        searchByCity = request.POST.get('optionCity') == 'on'

        if searchByName and searchByCity:
            spots = ToutistSpots.objects.filter(
                name__icontains=keyword
            ) | ToutistSpots.objects.filter(
                city__icontains=keyword
            )
        elif searchByName:
            spots = ToutistSpots.objects.filter(name__icontains=keyword)
        elif searchByCity:
            spots = ToutistSpots.objects.filter(city__icontains=keyword)
        else:
            spots = __getSpots()
            
        return render(request, 'touristSpotModule/spotList.html', {'spots': spots})
    else:
        return render(request, 'touristSpotModule/search.html')
