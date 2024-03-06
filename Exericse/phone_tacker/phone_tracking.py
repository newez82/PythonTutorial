"""
    1. folium module is to generate a map after getting person's location (Aerial view)
    2. argparse module is to accept input from users when runnign scripts from the terminal
    3. geocoder module is for geocoding phone numbers, providing informatino about the 
    geographic location
    4. coloarama is add colors to our output
"""


import argparse
import os
import sys

import folium
import phonenumbers
from colorama import Fore, init
from phonenumbers import carrier, geocoder, timezone


def process_number(phonenumber):
    """
    track phone number
    """
    try:
        global location
        parsed_number = phonenumbers.parse(phonenumber)
        location = geocoder.description_for_number(parsed_number, "en")
        country = geocoder.country_name_for_number(parsed_number, "en")
        print(
            f"{Fore.GREEN}[+] Attempting to track location of "
            f"{phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}.."
        )

        print(
            f"{Fore.GREEN}[+] Time Zone ID "
            f"{timezone.time_zones_for_number(parsed_number)}"
        )

        print(f"{Fore.GREEN}[+] Region: {location}")
        print(f"{Fore.GREEN}[+] Country: {country}")
        print(
            f"{Fore.GREEN}[+] Service Provider: {carrier.name_for_number(parsed_number, 'en')}"
        )

    except phonenumbers.phonenumberutil.NumberParseException:
        print(
            f"{Fore.RED}[-] Please specify a valid phone number (with country code)"
            f"or check your internet connection."
        )
        sys.exit()


def get_approx_coordinates():
    """ """
    from opencage.geocoder import OpenCageGeocode

    try:
        coder = OpenCageGeocode("6d6f969fd9024ac8afde957f0c86a5ba")
        query = location
        results = coder.geocode(query)
        latitude = results[0]["geometry"]["lat"]
        longitude = results[0]["geometry"]["lng"]
        print(f"[+] Latitude: {latitude}, Longitude: {longitude}")
        address = coder.reverse_geocode(latitude, longitude)
        address = address[0]["formatted"]
        print(f"{Fore.LIGHTRED_EX}[+] Approximate Location is {address}")
    except phonenumbers.phonenumberutil.NumberParseException:
        print(
            f"{Fore.RED}[-] Please specify a valid phone number (with country code)"
            f"or check your internet connection."
        )
        sys.exit()


process_number("+16463460876")
get_approx_coordinates()
