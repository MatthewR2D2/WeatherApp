'''
Simple Equation to convert kelvin to celsius temperature
c = k -273.15
'''
def kelvin_to_celsius(k):
    return round(k - 273.15, 2)

'''
This method will get the temperature out from the weather report
'''
def process_weather_temperature(weather_report):
    # store the value of "main"
    basic_stats = weather_report["main"]

    # store the value corresponding for current temperature pressure and humidity
    current_temperature = kelvin_to_celsius(basic_stats["temp"])
    feels_like = kelvin_to_celsius(basic_stats["feels_like"])
    min_temerature = kelvin_to_celsius(basic_stats["temp_min"])
    max_temperature = kelvin_to_celsius(basic_stats["temp_max"])
    current_pressure = basic_stats["pressure"]
    current_humidiy = basic_stats["humidity"]
    return current_temperature, feels_like, min_temerature, max_temperature, current_pressure, current_humidiy

'''
Helper method for parsing Json files that may have missing values
'''
def validate_json(json_text, text_needed):
    try:
        value = json_text[text_needed]
    except:
        value = None
    return value
'''
This method will get the general weather conditions from the report
'''
def process_weather_conditions(weather_report):
    # store the value of "weather"
    weather = weather_report["weather"]

    # to the "description" key at the 0th index of z

    weather_base_conditions = validate_json(weather[0],"main")
    weather_description = validate_json(weather[0],"description")
    weather_icon = validate_json(weather[0],"icon")
    viz = validate_json(weather_report, "visibility")
    wind_condition = validate_json(weather_report, "wind")
    wind_speed = validate_json(wind_condition, "speed")
    wind_dir = validate_json(wind_condition, "deg")
    return weather_base_conditions, weather_description, weather_icon, viz, wind_speed, wind_dir

'''
This method will get the location information from the report
'''
def process_weather_location(weather_report):
    name = validate_json(weather_report, "name")
    coordinates = validate_json(weather_report, "coord")
    long = validate_json(coordinates, "lon")
    lat = validate_json(coordinates, "lat")
    return name, long, lat

'''
This method converts degrees into cardinal directions
'''
def degrees_to_cardinal(deg):
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    card = round(deg / (360. / len(dirs)))
    return dirs[card % len(dirs)]