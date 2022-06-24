from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
from pymavlink import mavutil  # Needed for command message definitions
import time
import math
import datetime
import cv2
import time
import os
import argparse


tm = datetime.datetime.now()
current_date = tm.strftime('%Y')+tm.strftime("%m")+tm.strftime("%d")
print(current_date)
dir_path = f'/home/pi/DB_image/{current_date}'


if not os.path.isdir(dir_path):
    os.mkdir(dir_path)

capture = cv2.VideoCapture(0) 
img_counter = 0
# Set up option parsing to get connection string

def capture_img(img_counter):
    if (capture.isOpened):

        ret, frame = capture.read()
        
        if ret == False:
            pass
        frame = cv2.rotate(frame,cv2.ROTATE_180)
        #cv2.imshow("VideoFrame", frame)
        #now = datetime.datetime.now().strftime("%d_%H-%M-%S")
        key = cv2.waitKey(33)  # 1) & 0xFF

        current_lat = vehicle.location.global_relative_frame.lat
        current_lon = vehicle.location.global_relative_frame.lon	
        current_lat = "%0.4f" % (current_lat - int(current_lat))
        current_lon = "%0.4f" % (current_lon - int(current_lon))
        tm = datetime.datetime.now()
        current_time = tm.strftime('%H')+tm.strftime("%M")+tm.strftime("%S")
        print(current_time)
        print(current_lat[2:])
        print(current_lon[2:])
        
        cv2.IMREAD_UNCHANGED
        cv2.imwrite(f"{dest_dir_path}/{current_time}_{current_lat[2:]}{current_lon[2:]}.jpg", frame) # frame=컬러 화면 출력
        print('Saved frame%d.jpg' % img_counter)
        img_counter += 1

def Get_image(snd):
    cnt=0
    while (cnt < snd):
        capture_img(cnt)
        time.sleep(1)
        cnt +=1



def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()
    
    connection_string = args.connect
    baud_rate = 57600
    
    vehicle = connect(connection_string,baud=baud_rate,wait_ready=True)
    return vehicle

vehicle = connectMyCopter()  #GOTO SKY!
start_lat = vehicle.location.global_relative_frame.lat
start_lon = vehicle.location.global_relative_frame.lon	
start_lat = "%0.4f" % (start_lat - int(start_lat))
start_lon = "%0.4f" % (start_lon - int(start_lon))
start_location = start_lat[2:]+start_lon[2:]
tm = datetime.datetime.now()
start_time = tm.strftime('%H')+tm.strftime("%M")+tm.strftime("%S")


dir_path = f'/home/pi/DB_image/{current_date}'
dest_dir_path = f'/home/pi/DB_image/{current_date}/{start_time}_{start_location}'
if not os.path.isdir(dest_dir_path):
    os.mkdir(dest_dir_path)



def send_attitude_target(roll_angle=0.0, pitch_angle=0.0,
                         yaw_angle=None, yaw_rate=0.0, use_yaw_rate=False,
                         thrust=0.5):
    if yaw_angle is None:
        # this value may be unused by the vehicle, depending on use_yaw_rate
        yaw_angle = vehicle.attitude.yaw
    # Thrust >  0.5: Ascend
    # Thrust == 0.5: Hold the altitude
    # Thrust <  0.5: Descend
    msg = vehicle.message_factory.set_attitude_target_encode(
        0,  # time_boot_ms
        1,  # Target system
        1,  # Target component
        0b00000000 if use_yaw_rate else 0b00000100,
        to_quaternion(roll_angle, pitch_angle, yaw_angle),  # Quaternion
        0,  # Body roll rate in radian
        0,  # Body pitch rate in radian
        math.radians(yaw_rate),  # Body yaw rate in radian/second
        thrust  # Thrust
    )
    vehicle.send_mavlink(msg)


def set_attitude(roll_angle=0.0, pitch_angle=0.0,
                 yaw_angle=None, yaw_rate=0.0, use_yaw_rate=False,
                 thrust=0.5, duration=0):
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


def to_quaternion(roll=0.0, pitch=0.0, yaw=0.0):
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


# Take off 2.5m in GUIDED_NOGPS mode.
def arm_and_takeoff(aTargetAltitude):

    print("Basic pre-arm checks")
# Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)
    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
# Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)
        
        
    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude
# Wait until the vehicle reaches a safe height before processing the goto
# (otherwise the command after Vehicle.simple_takeoff will execute
# immediately).

    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)
        
        
arm_and_takeoff(2)

print("Hold position for 1 seconds")
set_attitude(duration=1)

print("Set default/target airspeed to 3")
vehicle.airspeed = 10

print("Going towards first point for 30 seconds ...")
point1 = LocationGlobalRelative(37.3409961, 126.7316986, 5)
# vehicle.simple_goto(point1,groundspeed=1) #high than takeoff_attitude
vehicle.simple_goto(point1)  # high than takeoff_attitude
# sleep so we can see the change in map

Get_image(15)

print("Going towards second point for 30 seconds ...")
point2 = LocationGlobalRelative(37.3406941, 126.7314444, 5)
# vehicle.simple_goto(point1,groundspeed=1) #high than takeoff_attitude
vehicle.simple_goto(point2)  # high than takeoff_attitude
# sleep so we can see the change in map
Get_image(10)

print("Going towards second point for 30 seconds ...")
point3 = LocationGlobalRelative(37.3405781, 126.7318426, 6)
# vehicle.simple_goto(point1,groundspeed=1) #high than takeoff_attitude
vehicle.simple_goto(point3)  # high than takeoff_attitude
# sleep so we can see the change in map
Get_image(12)

print("Going towards second point for 30 seconds ...")
point4 = LocationGlobalRelative(37.3407221, 126.7320782, 6)
# vehicle.simple_goto(point1,groundspeed=1) #high than takeoff_attitude
vehicle.simple_goto(point4)  # high than takeoff_attitude
# sleep so we can see the change in map
Get_image(10)

print("Setting LAND mode...")
vehicle.mode = VehicleMode("LAND")
time.sleep(10)

# Close vehicle object before exiting script
print("Close vehicle object")
vehicle.close()

# Shut down simulator if it was started.


print("Completed")
camera_test.capture.release()
camera_test.cv2.destroyAllWindows()

if sitl is not None:
    sitl.stop()
