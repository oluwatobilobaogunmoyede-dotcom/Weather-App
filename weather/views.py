from django.shortcuts import render
import requests


def weather(request):

    if request.method == "POST":
        city = request.POST["city"]

        source = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=09516e89f9da82d480004031038c3f01"

        list_of_data = requests.get(source.format(city)).json()

        data = {
            "country_code": str(list_of_data["sys"]["country"]),
            "coordinate": str(list_of_data["coord"]["lon"]) + ", "
                          + str(list_of_data["coord"]["lat"]),
            "temp": round((list_of_data["main"]["temp"] - 32) * 5 / 9, 2),
            "humidity": str(list_of_data["main"]["humidity"]),
        }

    else:
        data = {}

    return render(request, "weather.html", data)