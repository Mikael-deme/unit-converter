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
        1: {"name": "meter", "factor": 1},
        2: {"name": "kilometer", "factor": 1000},
        3: {"name": "hectometer", "factor": 100},
        4: {"name": "decameter", "factor": 10},
        5: {"name": "decimeter", "factor": 0.1},
        6: {"name": "centimeter", "factor": 0.01},
        7: {"name": "millimeter", "factor": 0.001},
        8: {"name": "mile", "factor": 1609.344},
        9: {"name": "yard", "factor": 0.9144},
        10: {"name": "foot", "factor": 0.3048},
        11: {"name": "inch", "factor": 0.0254}
    },
    
    "mass": {
        1: {"name": "gram", "factor": 1},
        2: {"name": "kilogram", "factor": 1000},
        3: {"name": "hectogram", "factor": 100},
        4: {"name": "decagram", "factor": 10},
        5: {"name": "decigram", "factor": 0.1},
        6: {"name": "centigram", "factor": 0.01},
        7: {"name": "milligram", "factor": 0.01},
        8: {"name": "ounce", "factor": 28.349523125},
        9: {"name": "pound", "factor": 453.59237},
        10: {"name": "US ton (short)", "factor": 907184.74}
    },
    
    "volume": {
        1: {"name": "cubic decimeter", "factor": 1},
        2: {"name": "cubic centimeter", "factor": 0.001},
        3: {"name": "teaspoon", "factor": 0.00492892159375},
        4: {"name": "tablespoon", "factor": 0.01478676478125},
        5: {"name": "US fluid ounce", "factor": 0.0295735295625},
        6: {"name": "US cup", "factor": 0.2365882365},
        7: {"name": "US liquid pint", "factor": 0.473176473},
        8: {"name": "US liquid quart", "factor": 0.946352946},
        9: {"name": "US liquid gallon", "factor": 3.785411784}        
    },
    
    "area": {
        1: {"name": "square meter", "factor": 1},
        2: {"name": "square kilometer", "factor": 1000000},
        3: {"name": "square hectometer", "factor": 10000},
        4: {"name": "square decameter", "factor": 100},
        5: {"name": "square decimeter", "factor": 0.01},
        6: {"name": "square centimeter", "factor": 0.0001},
        7: {"name": "square millimeter", "factor": 0.000001},
        8: {"name": "hectare", "factor": 10000},
        9: {"name": "acre", "factor": 4046.8564224},
        10: {"name": "square foot", "factor": 0.09290304}
    },

    "speed": {
        1: {"name": "meter per second", "factor": 1},
        2: {"name": "kilometer per hour", "factor": 0.2777777778},
        3: {"name": "mile per hour", "factor": 0.44704},
        4: {"name": "knot", "factor": 0.5144444444},
        5: {"name": "foot per second", "factor": 0.3048}
    },

    "temperature": {
        1: {"name": "kelvin"},
        2: {"name": "celcius"},
        3: {"name": "fahrenheit"}
    }
}

#Input the quantity index
quantity_index = int(input("Input the quantity index:\n"))

#Respectively, inputs for the original and destiny units and value
original_unit = int(input("Input the original unit index:\n"))
destiny_unit = int(input("Input the destiny unit index:\n"))
Value = float(input("Input the value:\n"))