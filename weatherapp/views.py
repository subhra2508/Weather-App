from django.shortcuts import render
import json
import requests
from django.contrib import messages

# Create your views here.
def weatherView(request):
    url="http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=feab60c549aaebe553e83bf8f0082541"
    city="bhubaneswar"
    if request.method=="POST":
        cityName=request.POST.get('cityvalue')
        city=cityName
    r=requests.get(url.format(city)).json()
    city_weather={
        'city':city,
        'temperature':r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon'],
    }
    context={'city_weather':city_weather}
    return render(request,'weatherapp/main.html',context)
