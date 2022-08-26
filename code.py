# =============================================================================
# The requests module allows you to send HTTP requests using Python.
# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).
# pip install request
# =============================================================================
import requests
print("Weather forecasting with Python, By: Anuj Patel ")
#input the city name
city = input('Enter the City : ')
print('Showing weather forecast for ',city)


#Display the message!
print('Displaying Weater report for: ' + city)

#fetch the weater details
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

#display the result!
print(res.text)