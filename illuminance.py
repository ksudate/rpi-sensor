import smbus
import datetime

Bus = smbus.SMBus(1)
Addr = 0x23

def main():
    path_illu ='/home/pi/log/illuminance.log'
    today = datetime.datetime.today().strftime("%Y/%m/%d %H:%M")
    LxRead = Bus.read_i2c_block_data(Addr,0x11)
    with open(path_illu, mode='a') as f:
        f.write(f'{today} {LxRead[1]*10}\n')

    #LxRead2 = Bus.read_i2c_block_data(Addr,0x10)
    #print(str((LxRead2[0] * 256 + LxRead2[1]) / 1.2))

if __name__=="__main__":
    main()
