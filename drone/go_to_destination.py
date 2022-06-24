from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
from pymavlink import mavutil  # Needed for command message definitions
import time
import math

# Set up option parsing to get connection string
import argparse


def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()
    
    connection_string = args.connect
    baud_rate = 57600
    
    vehicle = connect(connection_string,baud=baud_rate,wait_ready=True)
    return vehicle

vehicle = connectMyCopter()




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
        
        
arm_and_takeoff(3)

print("Hold position for 1 seconds")
set_attitude(duration=1)

print("Set default/target airspeed to 3")
vehicle.airspeed = 10

print("Going towards first point for 30 seconds ...")
point1 = LocationGlobalRelative(37.3409961, 126.7316986, 5)
# vehicle.simple_goto(point1,groundspeed=1) #high than takeoff_attitude
vehicle.simple_goto(point1)  # high than takeoff_attitude
# sleep so we can see the change in map
time.sleep(15)

print("Going towards second point for 30 seconds ...")
point2 = LocationGlobalRelative(37.3406941, 126.7314444, 5)
# vehicle.simple_goto(point1,groundspeed=1) #high than takeoff_attitude
vehicle.simple_goto(point2)  # high than takeoff_attitude
# sleep so we can see the change in map
time.sleep(10)

print("Going towards second point for 30 seconds ...")
point3 = LocationGlobalRelative(37.3405781, 126.7318426, 6)
# vehicle.simple_goto(point1,groundspeed=1) #high than takeoff_attitude
vehicle.simple_goto(point3)  # high than takeoff_attitude
# sleep so we can see the change in map
time.sleep(12)

print("Going towards second point for 30 seconds ...")
point4 = LocationGlobalRelative(37.3407221, 126.7320782, 6)
# vehicle.simple_goto(point1,groundspeed=1) #high than takeoff_attitude
vehicle.simple_goto(point4)  # high than takeoff_attitude
# sleep so we can see the change in map
time.sleep(10)

print("Setting LAND mode...")
vehicle.mode = VehicleMode("LAND")
time.sleep(10)

# Close vehicle object before exiting script
print("Close vehicle object")
vehicle.close()

# Shut down simulator if it was started.
if sitl is not None:
    sitl.stop()

print("Completed")


