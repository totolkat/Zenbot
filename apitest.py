import json
from colorama import Fore

with open("The_API.json", "r") as busapi:
    try:
        yay = input("Enter the bus plate.")
        n = yay.upper()
        n = yay.replace(" ", "")
        read = busapi.read()
        jread = json.loads(read)


        number = jread["results"][0][n]["number"]
        regplate = jread["results"][0][n]["reg_plate"]
        chassis = jread["results"][0][n]["chassis"]
        bodywork = jread["results"][0][n]["bodywork"]
        engine = jread["results"][0][n]["engine"]
        livery = jread["results"][0][n]["livery"]
        branding = jread["results"][0][n]["branding"]
        depot = jread["results"][0][n]["depot"]

        print(f"Results for: {n}\n\nNumber: {number}\nRegistration Plate: {regplate}\nChassis: {chassis}\nBodywork: {bodywork}\nEngine: {engine}\nLivery: {livery}\nBranding: {branding}\nDepot: {depot}")
    except KeyError:
        print("I couldn't find that registration plate.")
    
