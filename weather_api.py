import requests
city = input("What city are you from?: ").upper()

package = {
    'APPID': "591bd69a0b6c0fef91d7e9cc60883174",
    "q": city
}
r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)

data = r.json()
# print(data["weather"]["main"]

t_type = data["weather"][0]['main']
d_type = data["weather"][0]['description']
wind_speed = (data['wind']['speed'])
wind_direction = (data['wind']['deg'])
temp = (data ['main']['temp'])
c = temp-273.15
f = temp * 9/5 - 459.67
m = "Well in {} it is {} with {} and wind blowing at {} mph at {} degrees.".format(city, t_type, d_type, wind_speed, wind_direction)
# print(data)
# print(data["weather"]["description"])
print("Well it is {} kelvin in {} ".format(temp, city))
responce = input("press 'c' for celcius 'f' for fahrenheit or 'm' for more press \n:")
if responce is c:
    print(c)
elif responce is f:
    print(temp*9/5 - 459.67)
elif responce is m:
    print("Well in {} it is {} with {} and wind blowing at {} mph at {} degrees.".format(city, t_type, d_type, wind_speed, wind_direction))


# print(data['value']['joke'])
# r = request.post()
# Lab: PyWeather

'''
Create a program that will propt a user for city name or zip code.
Use that information to get the current weather. Display that information
to the user in a clean way.
## Advanced

* Also ask the user if they would like to see the results in C or F.

'''
