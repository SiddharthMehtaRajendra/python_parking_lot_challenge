import random
import string
import boto3
from parkinglot import ParkingLot
from car import Car
from dotenv import load_dotenv
import os

load_dotenv()

consumed_license_plate_numbers = []

def generate_license_plate_number():
    # Generate a random 7-digit alphanumeric string
    license_plate_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    return license_plate_number

def run_program():
    parkinglot = ParkingLot(parking_area_size=2000)

    cars_to_park = []
    while True:
        if len(consumed_license_plate_numbers) == 20:
            break
        random_license_plate_number = generate_license_plate_number()
        if random_license_plate_number in consumed_license_plate_numbers:
            continue
        consumed_license_plate_numbers.append(random_license_plate_number)
        cars_to_park.append(Car(f"{random_license_plate_number}"))
    while len(cars_to_park) > 0 and parkinglot.is_available():
        cars_to_park.pop().park(parkinglot)

    print("All the cars have been parked!")

    # Save the parking lot to a JSON file
    parkinglot.dump_to_json("parkinglot.json")

    # Upload the file to S3
    upload_to_s3("parkinglot.json", os.getenv("S3_BUCKET_NAME"), os.getenv("S3_FILE_KEY"))

def upload_to_s3(filename, bucket_name, file_key):
    s3 = boto3.client('s3')
    with open(filename, 'rb') as file:
        s3.upload_file(filename, bucket_name, file_key)
    print(f"File uploaded to S3 bucket: {bucket_name}, file key: {file_key}")

if __name__ == "__main__":
    run_program()
