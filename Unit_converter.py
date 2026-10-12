#Calculation for converting all the units that have a conversion factor
def conversion_factors_calculation(original_unit_factor, destiny_unit_factor, value):
    result = (value * original_unit_factor) / destiny_unit_factor
    
    return result

#Calculations for converting temperatures
def temperature_calculator( original_temperature, destiny_temperature, value):
    
    match original_temperature:
        case "kelvin":
            if destiny_temperature == "fahrenheit":
                result = 1.8 * (value - 273.15) + 32
            else:
                result = value - 273.15
        
        case "celcius":
            if destiny_temperature == "fahrenheit":
                result = (value * 1.8) + 32
            else:
                result = value + 273.15
        
        case "fahreneit":
            if destiny_temperature == "kelvin":
                result = (value - 32) / 1.8 + 273.15
            else:
                result = (value - 32) / 1.8
        
        case _:
            print(f"Something went wrong while converting {value} {original_temperature} to {destiny_temperature}!")
        
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
        2: {"name": "celcius", "symbol": "°F",},
        3: {"name": "fahrenheit", "symbol": "°C",}
    }
}


#Run through the quantities dictionary
print("SUPPORTED QUANTITIES:\n")
for index, quantity in quantities.items():
    print(f"{index} - {quantity}")
    
#Input the quantity index
quantity_index = int(input("\nInput the quantity index:\n"))

#store the selected quantity
selected_quantity = quantities[quantity_index]


#Run through the units dictionary
print("\nSUPORTED UNITS\n")
for index, unit in units[selected_quantity].items():
   print(f"Index: {index:>2} | Name: {unit["name"]:<18} | Symbol: {unit["symbol"]}")
    
#Respectively, inputs for the original and destiny units and value
original_unit = int(input("\nInput the original unit index:\n"))
destiny_unit = int(input("Input the destiny unit index:\n"))
value = float(input("Input the value:\n"))


#Separate the temperature function call from the other units's function
if selected_quantity =="temperature":
    #Store the name of the original and destiny temperature units
    original_temp = units[selected_quantity][original_unit]["name"]
    destiny_temp = units[selected_quantity][destiny_unit]["name"]

    print(temperature_calculator(original_temp, destiny_temp, value))
    
else:
    #Store the factors of the original and destiny units
    original_factor = units[selected_quantity][original_unit]["factor"]
    destiny_factor = units[selected_quantity][destiny_unit]["factor"]

    print(conversion_factors_calculation(original_factor, destiny_factor, value))