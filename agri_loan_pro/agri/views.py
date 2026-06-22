from django.shortcuts import render

# Create your views here.

def index(request):
   
    return render(request, "index.html")

def predict(request):
    if request.method == "POST":
        # Extract form data from POST request
        age = request.POST.get('age')
        land_area = request.POST.get('land_area')
        soil_type = request.POST.get('soil_type')
        sunlight_hours = request.POST.get('sunlight_hours')
        water_freq = request.POST.get('water_freq')
        fertilizer_type = request.POST.get('fertilizer_type')
        temperature = request.POST.get('temperature')
        humidity = request.POST.get('humidity')
        past_loan_status = request.POST.get('past_loan_status')
        income = request.POST.get('income')
        loan_amount_requested = request.POST.get('loan_amount_requested')
        
        # Print all variables to console
        print("=" * 50)
        print("FORM DATA RECEIVED:")
        print("=" * 50)
        print(f"Age: {age}")
        print(f"Land Area: {land_area}")
        print(f"Soil Type: {soil_type}")
        print(f"Sunlight Hours: {sunlight_hours}")
        print(f"Water Frequency: {water_freq}")
        print(f"Fertilizer Type: {fertilizer_type}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Past Loan Status: {past_loan_status}")
        print(f"Income: {income}")
        print(f"Loan Amount Requested: {loan_amount_requested}")
        print("=" * 50)
        
        # Convert numeric values to appropriate types
        try:
            age = float(age) if age else None
            land_area = float(land_area) if land_area else None
            sunlight_hours = float(sunlight_hours) if sunlight_hours else None
            temperature = float(temperature) if temperature else None
            humidity = float(humidity) if humidity else None
            income = float(income) if income else None
            loan_amount_requested = float(loan_amount_requested) if loan_amount_requested else None
        except ValueError:
            return render(request, "pre.html", {"error": "Invalid input values"})
        
        # Create a dictionary with all variables
        data = {
            'age': age,
            'land_area': land_area,
            'soil_type': soil_type,
            'sunlight_hours': sunlight_hours,
            'water_freq': water_freq,
            'fertilizer_type': fertilizer_type,
            'temperature': temperature,
            'humidity': humidity,
            'past_loan_status': past_loan_status,
            'income': income,
            'loan_amount_requested': loan_amount_requested
        }
        
        # TODO: Add prediction logic here using the data
        result = "Prediction pending"
        
        return render(request, "pre.html", {"result": result, "data": data})
   
    return render(request, "pre.html")