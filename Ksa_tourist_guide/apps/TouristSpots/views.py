from django.shortcuts import render, redirect

def index(request):
    # this view returns index
    return render(request, 'touristSpotModule/index.html')

def spots(request):
    return render(request, 'touristSpotModule/spotList.html')

def spot(request, sId):
    
    spot1 = {'id':12344321, 'name':'Al Khobar', 'description':'A vibrant city in the Eastern Province of KSA'}
    spot2 = {'id':56788765, 'name':'Najran', 'description':'A city rich with history in the southern region of KSA'}
    
    targetSpot = None
    if spot1['id'] == sId: targetSpot = spot1
    if spot2['id'] == sId: targetSpot = spot2
    
    if targetSpot == None: return redirect('/spots')
    
    context = {'spot':targetSpot} # spot is the variable name accessible by template
    return render(request, 'TouristSpotModule/spot.html', context)
