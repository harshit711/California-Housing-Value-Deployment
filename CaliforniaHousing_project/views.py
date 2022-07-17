from django.http import HttpResponse
from django.shortcuts import render
import pickle
import lzma


def home(request):
    cls = pickle.load(lzma.open("model.pickle", "rb"))
    county = pickle.load(open("county.pickle", "rb"))
    road = pickle.load(open("road.pickle", "rb"))
    city = pickle.load(open("city.pickle", "rb"))

    county_val = county.values()
    road_val = road.values()
    city_val = city.values()

    if request.method == 'POST':
        ls = list()
        ls1 = list()

        a = request.POST['MedInc']
        b = request.POST['HouseAge']
        c = request.POST['AveBedrms']
        d = request.POST['Population']
        e = request.POST['AveOccup']
        f = request.POST['County']
        g = request.POST['Road']
        h = request.POST['City']

        ls1.append(a)
        ls1.append(b)
        ls1.append(c)
        ls1.append(d)
        ls1.append(e)
        ls1.append(f)
        ls1.append(g)
        ls1.append(h)

        x = list(county.keys())[list(county.values()).index(f)]
        y = list(road.keys())[list(road.values()).index(g)]
        z = list(city.keys())[list(city.values()).index(h)]

        ls.append(a)
        ls.append(b)
        ls.append(c)
        ls.append(d)
        ls.append(e)
        ls.append(x)
        ls.append(y)
        ls.append(z)
        ans = cls.predict([ls])[0]
        ans = round(ans, 3)
        print(ans)
        return render(request, "home.html", {"ans": ans, "county_val": county_val, "road_val": road_val, "city_val": city_val, "a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g, "h": h})
    else:
        a = 0.0
        b = 0.0
        c = 0.0
        d = 0.0
        e = 0.0
        f = "Select County"
        g = "Select Road"
        h = "Select City"
    return render(request, "home.html", {"county_val": county_val, "road_val": road_val, "city_val": city_val, "a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g, "h": h})
