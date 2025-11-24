city = input("Enter your city name: ")

print("\n---- Weather Analyzer ----")

temp = float(input("Enter today's temperature in Celsius: "))

if temp > 30:
    suggestion = "It's very hot! Drink water and stay cool. ☀️"
elif temp > 20:
    suggestion = "Nice warm weather! Good day to go outside. 🙂"
elif temp > 10:
    suggestion = "A bit cold! You may need a light jacket. 🧥"
else:
    suggestion = "Very cold! Keep yourself warm. ❄️"

print(f"\nCity: {city}")
print(f"Temperature: {temp}°C")
print("Suggestion:", suggestion)