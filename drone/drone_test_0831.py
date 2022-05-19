from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
from pymavlink import mavutil
import time
import socket
#from pyexceptions import handle_exceptions
import math
import argparse

import RPi.GPIO as GPIO
import time
import camera_test
import datetime
import cv2






def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()
    
    connection_string = args.connect
    baud_rate = 921600
    
    vehicle = connect(connection_string,baud=baud_rate,wait_ready=True)
    return vehicle

def send_attitude_target(roll_angle = 0.0, pitch_angle = 0.0,
                         yaw_angle = None, yaw_rate = 0.0, use_yaw_rate = False,
                         thrust = 0.5):
   
  #  use_yaw_rate: the yaw can be controlled using yaw_angle OR yaw_rate.
  #                When one is used, the other is ignored by Ardupilot.
  #  thrust: 0 <= thrust <= 1, as a fraction of maximum vertical thrust.
  #          Note that as of Copter 3.5, thrust = 0.5 triggers a special case in
  #the code for maintaining current altitude.
    
    if yaw_angle is None:
        # this value may be unused by the vehicle, depending on use_yaw_rate
        yaw_angle = vehicle.attitude.yaw
    # Thrust >  0.5: Ascend
    # Thrust == 0.5: Hold the altitude
    # Thrust <  0.5: Descend
    msg = vehicle.message_factory.set_attitude_target_encode(
        0, # time_boot_ms
        1, # Target system
        1, # Target component
        0b00000000 if use_yaw_rate else 0b00000100,
        to_quaternion(roll_angle, pitch_angle, yaw_angle), # Quaternion
        0, # Body roll rate in radian
        0, # Body pitch rate in radian
        math.radians(yaw_rate), # Body yaw rate in radian/second
        thrust  # Thrust
    )
    vehicle.send_mavlink(msg)

def set_attitude(roll_angle = 0.0, pitch_angle = 0.0,
                 yaw_angle = None, yaw_rate = 0.0, use_yaw_rate = False,
                 thrust = 0.5, duration = 0):
    
   # Note that from AC3.3 the message should be re-sent more often than every
   # second, as an ATTITUDE_TARGET order has a timeout of 1s.
   # In AC3.2.1 and earlier the specified attitude persists until it is canceled.
   # The code below should work on either version.
   # Sending the message multiple times is the recommended way.
    
    send_attitude_target(roll_angle, pitch_angle,
                         yaw_angle, yaw_rate, False,
                         thrust)
    start = time.time()
    while time.time() - start < duration:
        send_attitude_target(roll_angle, pitch_angle,
                             yaw_angle, yaw_rate, False,
                             thrust)
        time.sleep(0.1)
    # Reset attitude, or it will persist for 1s more due to the timeout
    send_attitude_target(0, 0,
                         0, 0, True,
                         thrust)

def to_quaternion(roll = 0.0, pitch = 0.0, yaw = 0.0):
    
    t0 = math.cos(math.radians(yaw * 0.5))
    t1 = math.sin(math.radians(yaw * 0.5))
    t2 = math.cos(math.radians(roll * 0.5))
    t3 = math.sin(math.radians(roll * 0.5))
    t4 = math.cos(math.radians(pitch * 0.5))
    t5 = math.sin(math.radians(pitch * 0.5))

    w = t0 * t2 * t4 + t1 * t3 * t5
    x = t0 * t3 * t4 - t1 * t2 * t5
    y = t0 * t2 * t5 + t1 * t3 * t4
    z = t1 * t2 * t4 - t0 * t3 * t5

    return [w, x, y, z]
    
GPIO.setmode(GPIO.BCM)

trig = 3
echo = 2

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)




vehicle = connectMyCopter()
count = 1


while True :
    GPIO.output(trig, False)
    time.sleep(0.01)
    
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    print("done?")
    while GPIO.input(echo) == 0 :
        pulse_start = time.time()
        
    while GPIO.input(echo) == 1 :
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * (340*100) /2
    distance = round(distance,2)
    
    print("Distance : ", distance , "cm")
    #print(type(distance))
    print(vehicle.mode)
    
    if distance < 200 :
        vehicle.mode = VehicleMode("GUIDED_NOGPS")
        set_attitude(pitch_angle = 1, thrust = 0.8 , duration = 1)
        
    camera_test.capture_img(count)
    time.sleep(1)
    count +=1    



'''

count = 0

while(1):

    camera_test.capture_img(count)
    time.sleep(1)
    count +=1
'''    
    
    
