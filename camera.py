import picamera
import datetime

def main():
    imgdir_path = '/home/pi/img/'
    today = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M')
    img_path = imgdir_path + today + '.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (600,400)
        camera.capture(img_path)

if __name__=="__main__":
    main()
