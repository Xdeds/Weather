import requests
from django.shortcuts import render

# Create your views here.

# def main(request):
#     KEY = 'ac2ef8139be11eb96c7847fcc5b94875'
#     url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + KEY

#     city = 'Osh'
#     res = requests.get(url.format(city)).json()

#     info = {
#         'city': city,
#         'temp':res['main']['temp'],
#         # 'wind':res['main']['wind.speed']
#     }
#     context = {'info':info}
#     return render(request, 'index.html', context)


def main(request):
    KEY = 'ac2ef8139be11eb96c7847fcc5b94875'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + KEY

    city = 'Osh'
    res = requests.get(url.format(city)).json()

    info = {
        'city': city,
        'temp': res['main']['temp'],
        # 'wind':res['main']['wind.speed']
    }
    context = {'info': info}
    if request.method == 'POST':
        city = request.POST.get('city')
        KEY = '20fd2bf316d60ad758d379cf16f34627'
        API = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={KEY}'
        res = requests.get(API)
        data = res.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        max = data['main']['temp_max']
        min = data['main']['temp_min']
        sky = data['weather'][0]['main']
        icon = data['weather'][0]['icon']

        return render(request,
                      'index.html',
                      {'city': city,
                       'temp': temp,
                       'feels_like': feels_like,
                       'max': max,
                       'min': min,
                       'icon': icon,
                       'sky': sky})
    return render(request, 'index.html', context)
