#Calculation for converting all the units that have a conversion factor
def conversion_factors_calculation(source_unit_factor, target_unit_factor, value):
    if source_unit_factor == target_unit_factor:
        return value
    
    result = (value * source_unit_factor) / target_unit_factor
    return result

#Calculations for converting temperatures
def temperature_calculator( source_temperature, target_temperature, value):
    
    if source_temperature == target_temperature:
        return value
    
    match source_temperature:
        case "kelvin":
            if target_temperature == "fahrenheit":
                result = 1.8 * (value - 273.15) + 32
            else:
                result = value - 273.15
        
        case "celcius":
            if target_temperature == "fahrenheit":
                result = (value * 1.8) + 32
            else:
                result = value + 273.15
        
        case "fahrenheit":
            if target_temperature == "kelvin":
                result = (value - 32) / 1.8 + 273.15
            else:
                result = (value - 32) / 1.8
        
    return result


#Dictionary containing the supported quantities
quantities = {
    1: "length",
    2: "mass",
    3: "volume",
    4: "area",
    5: "speed",
    6: "temperature"
}

#Dictionary containing the supported units
units = {
    "length": {
        1: {"name": "meter", "symbol": "m", "factor": 1},
        2: {"name": "kilometer", "symbol": "km", "factor": 1000},
        3: {"name": "hectometer", "symbol": "hm", "factor": 100},
        4: {"name": "decameter", "symbol": "dam", "factor": 10},
        5: {"name": "decimeter", "symbol": "dm", "factor": 0.1},
        6: {"name": "centimeter", "symbol": "cm", "factor": 0.01},
        7: {"name": "millimeter", "symbol": "mm", "factor": 0.001},
        8: {"name": "mile", "symbol": "mi", "factor": 1609.344},
        9: {"name": "yard", "symbol": "yd", "factor": 0.9144},
        10: {"name": "foot", "symbol": "ft", "factor": 0.3048},
        11: {"name": "inch", "symbol": "in", "factor": 0.0254}
    },
    
    "mass": {
        1: {"name": "gram", "symbol": "g", "factor": 1},
        2: {"name": "kilogram", "symbol": "kg", "factor": 1000},
        3: {"name": "hectogram", "symbol": "hg", "factor": 100},
        4: {"name": "decagram", "symbol": "dag", "factor": 10},
        5: {"name": "decigram", "symbol": "dg", "factor": 0.1},
        6: {"name": "centigram", "symbol": "cg", "factor": 0.01},
        7: {"name": "milligram", "symbol": "mg", "factor": 0.01},
        8: {"name": "ounce", "symbol": "oz", "factor": 28.349523125},
        9: {"name": "pound", "symbol": "lb", "factor": 453.59237},
        10: {"name": "US short ton", "symbol": "US ton", "factor": 907184.74}
    },
    
    "volume": {
        1: {"name": "cubic decimeter",  "symbol": "dm3","factor": 1},
        2: {"name": "cubic centimeter", "symbol": "cm3", "factor": 0.001},
        3: {"name": "teaspoon", "symbol": "tsp", "factor": 0.00492892159375},
        4: {"name": "tablespoon", "symbol": "tbsp", "factor": 0.01478676478125},
        5: {"name": "US fluid ounce", "symbol": "fl oz", "factor": 0.0295735295625},
        6: {"name": "US cup", "symbol": "cup", "factor": 0.2365882365},
        7: {"name": "US liquid pint", "symbol": "pt", "factor": 0.473176473},
        8: {"name": "US liquid quart", "symbol": "qt", "factor": 0.946352946},
        9: {"name": "US liquid gallon", "symbol": "gal", "factor": 3.785411784}        
    },
    
    "area": {
        1: {"name": "square meter", "symbol": "m2", "factor": 1},
        2: {"name": "square kilometer", "symbol": "km2", "factor": 1000000},
        3: {"name": "square hectometer", "symbol": "hm2", "factor": 10000},
        4: {"name": "square decameter", "symbol": "dam2", "factor": 100},
        5: {"name": "square decimeter", "symbol": "dm2", "factor": 0.01},
        6: {"name": "square centimeter", "symbol": "cm2", "factor": 0.0001},
        7: {"name": "square millimeter", "symbol": "mm2", "factor": 0.000001},
        8: {"name": "hectare", "symbol": "ha", "factor": 10000},
        9: {"name": "acre", "symbol": "ac", "factor": 4046.8564224},
        10: {"name": "square foot", "symbol": "ft2", "factor": 0.09290304}
    },

    "speed": {
        1: {"name": "meter per second", "symbol": "m/s", "factor": 1},
        2: {"name": "kilometer per hour", "symbol": "km/h", "factor": 0.2777777778},
        3: {"name": "mile per hour", "symbol": "mph", "factor": 0.44704},
        4: {"name": "knot", "symbol": "kn", "factor": 0.5144444444},
        5: {"name": "foot per second", "symbol": "ft/s", "factor": 0.3048}
    },

    "temperature": {
        1: {"name": "kelvin", "symbol": "K",},
        2: {"name": "celcius", "symbol": "°C",},
        3: {"name": "fahrenheit", "symbol": "°F",}
    }
}


while True:
    
    #Run through the quantities dictionary
    print("SUPPORTED QUANTITIES:\n")
    for index, quantity in quantities.items():
        print(f"{index} - {quantity}")

    try:
        #Input the quantity index
        user = input("\nInput the quantity index:\n")
        quantity_index = int(user)
        
        if quantity_index < 1 or quantity_index > 6:
            raise ValueError
        
    except ValueError:
        print(f"\nPlease, type in the desired quantity index (only one).\nYour input was '{user}', which is unsuported.")
    else:
        break

#store the selected quantity
selected_quantity = quantities[quantity_index]


#Respectively, inputs for the source and target units and value
while True:
    
    #Run through the units dictionary 
    print("\nSUPORTED UNITS\n")
    
    if selected_quantity == "volume":
        print("\n1 cubic decimeter (dm3) = 1 liter (l)\n1 cubic centimeter (cm3) = 1 milliliter (ml)\n")
            
    for index, unit in units[selected_quantity].items():
        print(f"Index: {index:>2} | Name: {unit["name"]:<18} | Symbol: {unit["symbol"]}")

    try:
        user = input("\nInput the source unit index:\n")
        source_unit = int(user)
        if source_unit < 1 or source_unit > len(units[selected_quantity]):
            raise ValueError
        
        user = input("Input the target unit index:\n")
        target_unit = int(user)
        if target_unit < 1 or target_unit > len(units[selected_quantity]):
            raise ValueError
        
        user = input("Input the value:\n")
        value = float(user)
        
    except ValueError:
        print(f"\nPlease, type in the desired quantity index (only one).\nYour input was '{user}', which is unsuported.")
    else:
        break


#Separate the temperature function call from the other units's function
if selected_quantity =="temperature":
    
    #Store the names and symbols of the source and target temperature units
    source_temp = units[selected_quantity][source_unit]["name"]
    target_temp = units[selected_quantity][target_unit]["name"]
    
    source_symbol = units[selected_quantity][source_unit]["symbol"]
    target_symbol = units[selected_quantity][target_unit]["symbol"]

    temp_result = temperature_calculator(source_temp, target_temp, value)
    
    if temp_result >= 10**-4:
        print(f"\n\nThe conversion: {value} {source_temp} ({source_symbol}) to {target_temp} ({target_symbol})\nEquals: {temp_result:.4f} {target_symbol}")   
    else:
        print(f"\n\nThe conversion: {value} {source_temp} ({source_symbol}) to {target_temp} ({target_symbol})\nEquals: {temp_result} {target_symbol}")
    
else:
    #Store the factors, names and symbols of the source and target units
    source_factor = units[selected_quantity][source_unit]["factor"]
    target_factor = units[selected_quantity][target_unit]["factor"]
    
    source_name = units[selected_quantity][source_unit]["name"]
    source_symbol = units[selected_quantity][source_unit]['symbol']
    
    target_name = units[selected_quantity][target_unit]["name"]
    target_symbol = units[selected_quantity][target_unit]['symbol']

    factor_result = conversion_factors_calculation(source_factor, target_factor, value)
    
    if  factor_result >= 10**-4:
        print(f"\n\nThe conversion: {value} {source_name} ({source_symbol}) to {target_name} ({target_symbol})\nEquals: {factor_result:.4f} {target_symbol}")
    
    elif factor_result >= 10**-16:
        print(f"\n\nThe conversion: {value} {source_name} ({source_symbol}) to {target_name} ({target_symbol})\nEquals: {factor_result:.16f} {target_symbol}")
    else:
        print(f"\n\nThe conversion: {value} {source_name} ({source_symbol}) to {target_name} ({target_symbol})\nEquals: {factor_result} {target_symbol}")
        
        print(f"\nIt's a very small number.")