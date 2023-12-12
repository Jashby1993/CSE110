#The only creative thing I did was when the user wants to use celsius, the windchill displays in celsius as well.
#celsius to farenheit
def celsius_to_farenheit(degrees_celsius):
    temperature = (degrees_celsius * 9.0/5.0) + 32
    return temperature

#farenheit function
def get_windchill_f(temperature, wind_speed):
    windchill = 35.74 + (.6215 * temperature) - (35.75 * (wind_speed ** .16)) + (.4275 * temperature * (wind_speed ** .16))
    return windchill

#celsius function
def get_windchill_c(degrees_celsius,wind_speed):
    temperature = celsius_to_farenheit(degrees_celsius)    
    windchill_in_c = (get_windchill_f(temperature,wind_speed) - 32) * 5.0/9.0
    return windchill_in_c


degrees = float(input("How many degrees? "))

f_or_c = input("Do you use farenheit or celsius? Please type 'F' or 'C' only: ").lower()




if f_or_c == "f":
    for i in range(5,65,5):
        windchill = get_windchill_f(degrees,i)
        print(f"At temperature {degrees}F, and wind speed {i} mph, the windchill is: {windchill:.2f}F")

elif f_or_c == "c":
    for i in range(5,65,5):
        windchill = get_windchill_c(degrees, i)
        print(f"At temperature {degrees}C, and wind speed {i} mph, the windchill is: {windchill:.2f}C")

else:
    print("That was not a valid option, please type only 'F' or 'C'.")


