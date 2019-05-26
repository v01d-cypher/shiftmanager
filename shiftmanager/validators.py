import csv
import io
import os

from django.core.exceptions import ValidationError

REQUIRED_HEADER_EMPLOYEES  = ['First Name','Last Name']
REQUIRED_HEADER_SHIFTS  = ['Date', 'Start', 'End', 'Break']

def csv_file_validator(value):
    filename, ext = os.path.splitext(value.name)
    if  str(ext) != '.csv':
         raise ValidationError("Must be a csv file")

    if filename.find('employees') > -1:
        required_header = REQUIRED_HEADER_EMPLOYEES

    elif filename.find('shifts') > -1:
        required_header = REQUIRED_HEADER_SHIFTS

    decoded_file = value.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    reader = csv.reader(io_string, delimiter=',', quotechar='"')
    
    if next(reader) != required_header:
        raise ValidationError(f"Invalid File. Please use valid CSV Header for {value.name}")

    return True
