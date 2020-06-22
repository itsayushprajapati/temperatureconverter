#TempratureConverter

class Conversion:

  """\'Conversion\' class for conversion of temperature units .\n Use help for more -> help(temprature) """

  def __init__(self,cel=0, fahrenheit=0,kelvin=0):

    self.cel=cel

    self.fahrenheit=fahrenheit

    self.kelvin=kelvin

  def ctof(self):

    """Method to convert Celcuis to Fahrenheit"""

    var=self.cel*9+160

    fahrenheit=var/5

    return f"Temprature in Fahrenheit -> {fahrenheit}°F"

  def ctok(self):

    """Method to convert Celcius to Kelvin"""

    kelvin=self.cel+274.15

    return f"Temprature in Kelvin -> {kelvin}"

  def ftoc(self):

    """Method to convert Fahrenheit to Celcius"""

    var=(self.fahrenheit-32)/9

    celcius=var*5

    return f"Temprature in Celcius -> {celcius}°C"

  def ktoc(self):

    """Method to convert Kelvin to Celcius -- Coming Soon"""

    pass

  @property

  def info(self):

    return f"Celcius -> {self.cel}° Fahrenheit -> {self.fahrenheit}° Kelvin -> {self.kelvin}°"

class Defination:

  def __init__(self,status=False):

    self.status=status

  def getdef(self):

    if self.status==True:

      return f"Celcius - The Celsius scale, also known as the centigrade scale, is a temperature scale. As an SI derived unit, it is used worldwide. However, in the United States, the Bahamas, Belize, the Cayman Islands, and Liberia, Fahrenheit remains the preferred scale for everyday temperature measurement. The degree Celsius (symbol: °C) can refer to a specific temperature on the Celsius scale or a unit to indicate a difference between two temperatures or an uncertainty. -- Wiki\n\nFahrenheit - The Fahrenheit scale is a temperature scale based on one proposed in 1724 by physicist Daniel Gabriel Fahrenheit. It uses the degree Fahrenheit as the unit. Several accounts of how he originally defined his scale exist. -- Wiki \n\nKelvin - The kelvin is the base unit of temperature in the International System of Units (SI), having the unit symbol K. It is named after the Belfast-born, Glasgow University engineer and physicist William Thomson, 1st Baron Kelvin (1824–1907). -- Wiki"

    else:

      return "Turn Status to \'True\'"
