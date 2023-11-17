from django.shortcuts import render
from django.db import connection
from django.http import Http404

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

    # Fetch the search term
    search_words = []
    search_term = request.GET.get('search_term', '').strip()

    # Check if search term is not empty
    if search_term:
        search_words = search_term.split()

    # Initialize search_words as an empty list
    search_words = []

    # Fetch the search term
    search_term = request.GET.get('search_term', '').strip()

    # Check if search term is not empty
    if search_term:
        search_words = search_term.split()

        # Build the search query only if there are search words
        search_query = " AND ("
        search_query_parts = []
        for word in search_words:
            search_query_parts.append(
                "(make LIKE %s OR model LIKE %s OR exterior_color LIKE %s OR "
                "vehicle_description LIKE %s OR fuel_type LIKE %s OR CAST(year_of_production AS CHAR) LIKE %s)")
            params.extend(["%" + word + "%"] * 6)

        # Only append if there are parts to the search query
        if search_query_parts:
            search_query += " OR ".join(search_query_parts) + ")"
            query += search_query

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


def product_detail(request, listing_id):
    with connection.cursor() as cursor:
        # SQL query to join USERS and LISTED_VEHICLES tables
        cursor.execute("""
            SELECT LV.*, U.* 
            FROM LISTED_VEHICLES AS LV
            JOIN USERS AS U ON LV.seller_id = U.user_id
            WHERE LV.listing_id = %s
        """, [listing_id])

        result = cursor.fetchone()

    # If no product is found, raise a 404 error
    if not result:
        raise Http404("Product does not exist")

    # Map the result to a dictionary for easy access in the template
    product_dict = {
        'VIN': result[2],
        'image_url': result[4],
        'vehicle_description': result[5],
        'make': result[6],
        'model': result[7],
        'fuel_type': result[8],
        'year_of_production': result[9],
        'mileage': result[10],
        'price': result[11],
        'exterior_color': result[12],
        'interior_color': result[13],
        'state': result[14],
        'zip_code': result[15],
        'seller_name': result[22],
        'seller_rating': result[25],
    }

    return render(request, 'product_detail.html', {'product': product_dict})
