import datetime
import board
import busio
from adafruit_htu21d import HTU21D

i2c = busio.I2C(board.SCL, board.SDA)
sensor = HTU21D(i2c)

def main():
    path_temp = '/home/pi/log/temperature.log'
    path_hum = '/home/pi/log/humidity.log'
    today = datetime.datetime.today().strftime("%Y/%m/%d %H:%M")
    with open(path_temp, mode='a') as f:
        f.write("%s %0.1f\n" %(today, sensor.temperature))
    with open(path_hum, mode='a') as f:
        f.write("%s %0.1f\n" %(today, sensor.relative_humidity))

if __name__=="__main__":
   main()
