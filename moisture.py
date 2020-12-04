import time
import grovepi

sensor = 0
i = 0
data= []
while i < 10:
    data[i] = grovepi.analogRead(sensor)
    print(grovepi.analogRead(sensor))
    i += 1
    time.sleep(.5)

ave = sum(data)/len(data) 
print(ave)
