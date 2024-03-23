from django.shortcuts import render, redirect

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
    return [
        {'id': 1, 'name': 'Al-Ula', 'city': 'Al-Ula', 'description': 'Ancient city in the Medina Region, home to the UNESCO World Heritage site of Hegra', 'location': 'Al-Ula, Medina Region, Saudi Arabia'},
        {'id': 2, 'name': 'Kingdom Centre Tower', 'city': 'Riyadh', 'description': 'A 99-story, 302.3 m skyscraper in Riyadh, famous for its distinctive parabolic arch', 'location': '2239 King Fahd Rd, Al Olaya, Riyadh 12214, Saudi Arabia'},
        {'id': 3, 'name': 'Jeddah Corniche', 'city': 'Jeddah', 'description': 'Waterfront area along the Red Sea, with resorts, beaches, and art sculptures', 'location': 'Jeddah Corniche, Jeddah, Saudi Arabia'}
    ]