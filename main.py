import time
import smbus2
import RPi_I2C_driver
import bme280
# RPi_I2C_driver can be found here: https://gist.github.com/DenisFromHR/cc863375a6e19dce359d

def main():

  # sensor bme280
  port = 1
  sensor_address = 0x76
  bus = smbus2.SMBus(port)

  parametros_calibracao = bme280.load_calibration_params(bus, sensor_address)

  # display lcd
  mylcd = RPi_I2C_driver.lcd()

  try:

    while(1):
      data = bme280.sample(bus, sensor_address, parametros_calibracao)
      temperature = data.temperature
      pressure = data.pressure
      humidity = data.humidity
      print(type(temperature))
      print('t:{:.2f}, h:{:.2f}'.format(temperature, humidity))
      response = 't:{:.2f}, h:{:.2f}'.format(temperature, humidity)
      print('p:{:.2f}'.format(pressure))
      response2 = 'p:{:.2f}'.format(pressure)

      mylcd.lcd_display_string(response, 1)
      mylcd.lcd_display_string(response2, 2)
      time.sleep(1)
  
  except KeyboardInterrupt:
    print('finalizando...')

main()