from django.shortcuts import render
from django.db import connection

# Create your views here.


def searchCar(request):
    # Fetch unique values for dropdowns from the database
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT DISTINCT make FROM LISTED_VEHICLES ORDER BY make")
        makes = [row[0] for row in cursor.fetchall()]

        cursor.execute(
            "SELECT DISTINCT year_of_production FROM LISTED_VEHICLES ORDER BY year_of_production")
        years = [row[0] for row in cursor.fetchall()]

        cursor.execute(
            "SELECT DISTINCT mileage FROM LISTED_VEHICLES ORDER BY mileage")
        mileages = [row[0] for row in cursor.fetchall()]

        cursor.execute(
            "SELECT DISTINCT price FROM LISTED_VEHICLES ORDER BY price")
        prices = [row[0] for row in cursor.fetchall()]

    error_message = None

    # Fetch filter parameters
    make = request.GET.get('make')
    min_year = request.GET.get('min_year')
    max_year = request.GET.get('max_year')
    min_mileage = request.GET.get('min_mile')
    max_mileage = request.GET.get('max_mile')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Check for invalid filter ranges
    if min_year and max_year and int(min_year) > int(max_year):
        error_message = "Minimum year cannot be greater than maximum year."
    elif min_mileage and max_mileage and int(min_mileage) > int(max_mileage):
        error_message = "Minimum mileage cannot be greater than maximum mileage."
    elif min_price and max_price and int(min_price) > int(max_price):
        error_message = "Minimum price cannot be greater than maximum price."

    # If there's an error, return early with the error message
    if error_message:
        return render(request, 'searchCar.html', {'error_message': error_message})

# Initialize the base query
    query = "SELECT * FROM LISTED_VEHICLES WHERE 1=1"

    # Initialize the parameters list
    params = []

    # Append conditions to the query based on provided filters
    if make:
        query += " AND make = %s"
        params.append(make)

    if min_year:
        query += " AND year_of_production >= %s"
        params.append(min_year)

    if max_year:
        query += " AND year_of_production <= %s"
        params.append(max_year)

    if min_mileage:
        query += " AND mileage >= %s"
        params.append(min_mileage)

    if max_mileage:
        query += " AND mileage <= %s"
        params.append(max_mileage)

    if min_price:
        query += " AND price >= %s"
        params.append(min_price)

    if max_price:
        query += " AND price <= %s"
        params.append(max_price)

    vehicles = []
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        columns = [col[0] for col in cursor.description]
        for row in cursor.fetchall():
            vehicles.append(dict(zip(columns, row)))

    return render(request, 'searchCar.html', {
        'vehicles': vehicles,
        'makes': makes,
        'years': years,
        'mileages': mileages,
        'prices': prices,
        'error_message': error_message
    })
