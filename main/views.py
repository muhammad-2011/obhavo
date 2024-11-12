from django.shortcuts import render
from weather.ob_havo import Obhavo


def weather_view(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')  # Safely get the city value
        data = Obhavo(city=f'{city}').main()  # Call the main method on Obhavo
        
        # Check if data is None or if it doesn't contain expected keys
        if data and 'degree' in data and 'city' in data and 'day' in data:
            result = data['degree']
            city = data['city']
            day = data['day']
            context = {
                'degree': result,
                'city': city,
                'day': day
            }
        else:
            # Handle cases where data is None or missing keys
            context = {
                'error': 'Weather data could not be retrieved. Please try again.'
            }
        
        return render(request, 'index.html', context=context)
    
    # If GET request, simply render the form without context
    return render(request, 'index.html')
