import os
import time
import robot

print("Starting Program")
time.sleep(2)

print("Recording started - 10 seconds")
os.system("raspivid -w 640 -h 480 -fps 90 -t 30000 -o Testes.mp4")

robot.forward(1)
robot.forward(1)
robot.forward(1)
robot.forward(1)

print("Recording complete. Please wait.....")
time.sleep(2)

print("Video conversion complete")
time.sleep(2)

print("Closing program")
time.sleep(2)


