import json

class ParkingLot:
    def __init__(self, parking_area_size, parking_space_area_size=(8,12)):
        self.parking_area_size = parking_area_size
        self.parking_space_area_size = parking_space_area_size
        self.parking_spaces = self.initalize_parking_lot()

    def initalize_parking_lot(self):
        if self.parking_area_size is None or self.parking_space_area_size is None:
            raise Exception("Spot Area Size and/or Parking Area Size not specified")
        parking_space_total_area = self.parking_space_area_size[0] * self.parking_space_area_size[1]
        total_spots = self.parking_area_size // parking_space_total_area
        return [None] * total_spots

    def park(self, license_plate_number, parking_space_number):
        if parking_space_number < 0 or parking_space_number >= len(self.parking_spaces):
            raise Exception("Invalid parking space")
        if self.parking_spaces[parking_space_number] is None:
            self.parking_spaces[parking_space_number] = license_plate_number
            return (True, f"Car with license plate {license_plate_number} parked successfully in spot {parking_space_number}")
        elif self.parking_spaces[parking_space_number] is not None:
            return (False, f"Spot {parking_space_number} is already taken. Car with license plate {license_plate_number} cannot park here.")

    def is_available(self):
        return any(parking_space is None for parking_space in self.parking_spaces)

    def dump_to_json(self, filename):
        filled_spaces = {}
        for space_index, filled_space in enumerate(self.parking_spaces):
            if filled_space is not None:
                filled_spaces[space_index] = filled_space
            else:
                filled_spaces[space_index] = None
        with open(filename, 'w') as dump:
            json.dump(filled_spaces, dump)
