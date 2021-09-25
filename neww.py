from picamera import PiCamera
camera = PiCamera()
camera.resolution = (2592, 1944)
camera.framerate = 15
image = '/home/pi/Desktop/im.jpg'

camera.capture(image)
