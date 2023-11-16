from django.shortcuts import render
from .models import Employee

# Create your views here.
def testmysql(request):
    employee = Employee.objects.all()
    context = {
        'user_ssn': employee[0].ssn,
        'user_name': employee[0].lname,
    }
    return render(request, 'home.html', context)


def searchCar(request):
    # Car makes, sorted alphabetically
    makes = ["Audi", "BMW", "Chevrolet", "Ford", "Honda", "Hyundai", "Jeep", "Kia", "Lexus", "Mercedes", "Nissan", "Tesla", "Toyota", "Volkswagen"]

    # Year options
    years = [2016, 2017, 2018, 2019, 2020, 2021, 2022]

    # Mileage options (0 to 20000, step by 4000)
    mileages = list(range(0, 20001, 4000))

    # Price options (10000 to 35000, step by 5000)
    prices = list(range(10000, 35001, 5000))

    context = {
        'makes': makes,
        'years': years,
        'mileages': mileages,
        'prices': prices
    }

    return render(request, 'searchCar.html', context)