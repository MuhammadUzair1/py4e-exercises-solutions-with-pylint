"""
This script interacts with the Geoapify API (via a heavily rate-limited proxy) 
to retrieve latitude, longitude, formatted address, and plus code for a given location.
"""

import urllib.request
import urllib.parse
import json
import ssl
import os

# Heavily rate-limited proxy for https://www.geoapify.com/ API
SERVICE_URL = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

while True:
    # Input the location address
    full_address = input('Enter location: ').strip()
    if not full_address:
        break

    # Prepare parameters
    parameters = {'q': full_address}
    URL = SERVICE_URL + urllib.parse.urlencode(parameters)

    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Retrieve data
    print('Retrieving', URL)
    try:
        with urllib.request.urlopen(URL, context=CTX) as response:
            data = response.read().decode()
    except urllib.error.URLError as e:
        print(f"Failed to retrieve data: {e.reason}")
        break

    print('\nRetrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    # Parse JSON
    try:
        json_data = json.loads(data)
    except json.JSONDecodeError:
        print("Failed to parse JSON response.")
        break

    # Check for valid data
    if not json_data or 'features' not in json_data or not json_data['features']:
        print('==== Object not found or invalid response ====')
        print(data)
        break

    # Extract data
    properties = json_data['features'][0]['properties']
    latitude = properties['lat']
    longitude = properties['lon']
    formatted_address = properties['formatted']
    plus_code = properties['plus_code']

    # Display results
    print(f"\nLatitude: {latitude}, Longitude: {longitude}")
    print(f"\nAddress: {formatted_address}")
    print(f"\nPlus Code: {plus_code}")
