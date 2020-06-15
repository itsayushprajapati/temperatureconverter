#python program to convert celcius to fahrenheit
#Celcius and Farenhiet are two units for measuring temperature
def ctof(c):
    var=c*9+160
    fahrenheit=var/5
    return f"Temprature -> {fahrenheit}°F"
celcius=int(input("° Celcius : "))
print(ctof(celcius))
#url -> https://facebook.com/itsayushprajapati
#program ends here 
