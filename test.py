import picamera
import time
import robot


camera = picamera.PiCamera()
camera.start_recording('2.h264')
time.sleep(9)

robot.reverse(1)
robot.left(1)
robot.reverse(1)
robot.reverse(1)
robot.reverse(1)

camera.stop_recording()





