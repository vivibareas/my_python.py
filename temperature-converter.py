convertingdirection = input(" Do you want to convert a temperature in degrees Celsius to Fahrenheit or Fahrenheit to Celsius? ") # This makes the program ask a question
if convertingdirection == "degrees Celsius to Fahrenheit" or convertingdirection == "to degrees Fahrenheit":
    temperaturevalue = input(" How many degrees Celsius? ") # This makes the program ask a question
    if isinstance(temperaturevalue, int): # This detects whether the input is an int or float
        print(int(temperaturevalue) * 9 / 5 + 32)
    else:
        print(float(temperaturevalue) * 9 / 5 + 32)
elif convertingdirection == "degrees Fahrenheit to Celsius" or convertingdirection == "to degrees Celsius": # 'elif' stands for 'else if'
    temperaturevalue = input(" How many degrees Fahrenheit? ") # This makes the program ask a question
    if isinstance(temperaturevalue, int): # This detects whether the input is an int or float
        print(int((temperaturevalue - 32) * 5 / 9))
    else:
        print((float(temperaturevalue) - 32) * 5 / 9)
