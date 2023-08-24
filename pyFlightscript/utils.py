import os 

def check_valid_length_units(units):
    """
    Check if the provided input units are valid. 
    """
    valid_units = ["INCH", "MILLIMETER", "OTHER", "FEET", "MILE", "METER", "KILOMETER", 
                   "MILS", "MICRON", "CENTIMETER", "MICROINCH"]
    if units not in valid_units:
        raise ValueError(f"Invalid units: {units}. Must be one of {', '.join(valid_units)}.")
    return

def check_valid_force_units(units):
    """
    Check if the provided input units are valid. 
    """
    valid_units = ['COEFFICIENTS', 'NEWTONS', 'KILO-NEWTONS', 
                   'POUND-FORCE', 'KILOGRAM-FORCE']
    if units not in valid_units:
        raise ValueError(f"Invalid units: {units}. Must be one of {', '.join(valid_units)}.")
    return

def check_file_existence(file):
    # Validate file existence
    if not os.path.exists(file):
        raise FileNotFoundError(f"The specified file '{file}' does not exist.")
    return