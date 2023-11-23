import random

class Car:
    def __init__(self, license_plate_number, car_type='Standard Car'):
        if license_plate_number is None:
            raise Exception('Please provide license plate number')
        self.license_plate_number = license_plate_number
        self.car_type = car_type

    def __str__(self):
        return self.license_plate_number

    def park(self, parkinglot):
        print(f"Parking car of type {self.car_type} with license plate number {self.license_plate_number}")
        while True:
            if not parkinglot.is_available():
                break
            parking_space_number = random.randint(0, len(parkinglot.parking_spaces) - 1)
            result_status, result_string = parkinglot.park(self.license_plate_number, parking_space_number)
            print(result_string)
            if result_status is True:
                break
