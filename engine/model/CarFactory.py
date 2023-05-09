from Engine import CapuletEngine
from Engine import WilloughbyEngine
from Engine import SternmanEngine
from Battery import SpindlerBattery
from Battery import NubbinBattery
from car import Car
from itertools import combinations


class CarFactory:

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(current_date, last_service_date, warning_light_is_on, array):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def octoprime_tyres(array):
            for combination in combinations(array, 4):
                if sum(combination) >= 3:
                 return True
                else:
                 return False

    def carrigan_tyres(array):
        for value in array:
            if value == 0.9:
                return True
            else:
                return False

