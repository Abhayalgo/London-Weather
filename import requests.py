import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data(date):
    response = requests.get(API_URL)
    data = response.json()
    # Process the data to get the temperature for the input date
    # In this example, let's assume the API returns the temperature for the first data point
    temperature = data['list'][0]['main']['temp']
    return temperature

def get_wind_speed_data(date):
    response = requests.get(API_URL)
    data = response.json()
    # Process the data to get the wind speed for the input date
    # In this example, let's assume the API returns the wind speed for the first data point
    wind_speed = data['list'][0]['wind']['speed']
    return wind_speed

def get_pressure_data(date):
    response = requests.get(API_URL)
    data = response.json()
    # Process the data to get the pressure for the input date
    # In this example, let's assume the API returns the pressure for the first data point
    pressure = data['list'][0]['main']['pressure']
    return pressure

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Terminating the program.")
            break
        elif choice in (1, 2, 3):
            date = input("Enter the date (YYYY-MM-DD): ")

            if choice == 1:
                temp = get_weather_data(date)
                print(f"Temperature on {date}: {temp}")
            elif choice == 2:
                wind_speed = get_wind_speed_data(date)
                print(f"Wind Speed on {date}: {wind_speed}")
            elif choice == 3:
                pressure = get_pressure_data(date)
                print(f"Pressure on {date}: {pressure}")
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
