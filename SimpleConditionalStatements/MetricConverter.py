number = float(input())
input_metric = input()
output_metric = input()
meters = 0.0
millimeters = 0.0
centimeters = 0.0
miles = 0.0
inches = 0.0
kilometers = 0.0
feet = 0.0
yards = 0.0

if input_metric == "m":
    meters = number
    millimeters = number * 1000
    centimeters = number * 100
    miles = number * 0.000621371192
    inches = number * 39.3700787
    kilometers = number * 0.001
    feet = number * 3.2808399
    yards = number * 1.0936133
elif input_metric == "mm":
    millimeters = number
    meters = number / 1000
    centimeters = meters * 100
    miles = meters * 0.000621371192
    inches = meters * 39.3700787
    kilometers = meters * 0.001
    feet = meters * 3.2808399
    yards = meters * 1.0936133
elif input_metric == "cm":
    centimeters = number
    meters = number / 100
    millimeters = meters * 1000
    miles = meters * 0.000621371192
    inches = meters * 39.3700787
    kilometers = meters * 0.001
    feet = meters * 3.2808399
    yards = meters * 1.0936133
elif input_metric == "mi":
    miles = number
    meters = number / 0.000621371192
    millimeters = meters * 1000
    centimeters = meters * 100
    inches = meters * 39.3700787
    kilometers = meters * 0.001
    feet = meters * 3.2808399
    yards = meters * 1.0936133
elif input_metric == "in":
    inches = number
    meters = number / 39.3700787
    millimeters = meters * 1000
    centimeters = meters * 100
    miles = meters * 0.000621371192
    kilometers = meters * 0.001
    feet = meters * 3.2808399
    yards = meters * 1.0936133
elif input_metric == "km":
    kilometers = number
    meters = number / 0.001
    millimeters = meters * 1000
    centimeters = meters * 100
    miles = meters * 0.000621371192
    inches = meters * 39.3700787
    feet = meters * 3.2808399
    yards = meters * 1.0936133
elif input_metric == "ft":
    feet = number
    meters = number / 3.2808399
    millimeters = meters * 1000
    centimeters = meters * 100
    miles = meters * 0.000621371192
    inches = meters * 39.3700787
    kilometers = meters * 0.001
    yards = meters * 1.0936133
elif input_metric == "yd":
    yards = number
    meters = number / 1.0936133
    millimeters = meters * 1000
    centimeters = meters * 100
    miles = meters * 0.000621371192
    inches = meters * 39.3700787
    kilometers = meters * 0.001
    feet = meters * 3.2808399
if output_metric == "m":
    print("{0} m".format(meters))
elif output_metric == "mm":
    print("{0} mm".format(millimeters))
elif output_metric == "cm":
    print("{0} cm".format(centimeters))
elif output_metric == "mi":
    print("{0} mi".format(miles))
elif output_metric == "in":
    print("{0} in".format(inches))
elif output_metric == "km":
    print("{0} km".format(kilometers))
elif output_metric == "ft":
    print("{0} ft".format(feet))
elif output_metric == "yd":
    print("{0} yd".format(yards))
