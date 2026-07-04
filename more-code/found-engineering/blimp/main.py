"""
CONTRIBUTORS: @jasr4j, @mutong-daisy-hu
PURPOSE: CONTROL REMOTE FLIGHT ON A RASPBERRY PI ZERO W OVER WIFI
"""


from blimputils import Motor, Accelerometer, Gyroscope, Magnetometer
from datetime import datetime
from collections import defaultdict
import pigpio
import time

def log_data(accel, gyro, mag): 
  accel_data = accel.get_xyz()
  gyro_data = gyro.get_xyz()
  mag_data = mag.get_xyz()
  data = f"TIMESTAMP: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\nAccel: X={accel_data[0]}, Y={accel_data[1]}, Z={accel_data[2]}\nGyro: X={gyro_data[0]}, Y={gyro_data[1]}, Z={gyro_data[2]}\nMag: X={mag_data[0]}, Y={mag_data[1]}, Z={mag_data[2]}\n"
  with open("log.txt", "a") as file:
    file.write(data)

def collect_data(accel, gyro, mag):
  print("\n--- Sensor Readings ---")
  accel_data = accel.get_xyz()
  print(f"Accelerometer: X={accel_data[0]}, Y={accel_data[1]}, Z={accel_data[2]}")
  gyro_data = gyro.get_xyz()
  print(f"Gyroscope: X={gyro_data[0]}, Y={gyro_data[1]}, Z={gyro_data[2]}")
  mag_data = mag.get_xyz()
  print(f"Magnetometer: X={mag_data[0]}, Y={mag_data[1]}, Z={mag_data[2]}")
  s = f"Accelerometer: X={accel_data[0]}, Y={accel_data[1]}, Z={accel_data[2]}\n"
  s += f"Gyroscope: X={gyro_data[0]}, Y={gyro_data[1]}, Z={gyro_data[2]}\n"
  s += f"Magnetometer: X={mag_data[0]}, Y={mag_data[1]}, Z={mag_data[2]}\n"
  return s

def move(motors, rev, dir): 
  # DIRS: UP, DOWN, W, A, S, D
  # motorObject.spin(target_speed: int, ramp_type: str = None, ramp_duration: float = 0)
  motor1, motor2, motor3, motor4 = motors
  rm1, rm2, rm3, rm4 = rev
  ramp_type = 'log'
  speed = 50
  ramp_duration = 0.2
  duration = 5
  dirFormatter = defaultdict(lambda: "INVALID")
  dirFormatter["W"] = "FORWARD"
  dirFormatter["A"] = "LEFT"
  dirFormatter["S"] = "BACKWARD"
  dirFormatter["D"] = "RIGHT"
  print(f"<< MOVING IN THE {dirFormatter[dir]} DIRECTION FOR {duration} SECONDS")
  print(f"<< RAMP_TYPE={ramp_type}, SPEED={speed}, RAMP_DURATION={ramp_duration}")
  if dir == "UP": 
    motor3.spin(speed, ramp_type, ramp_duration)
    motor4.spin(speed, ramp_type, ramp_duration)
  elif dir == "W": 
    motor1.spin(speed, ramp_type, ramp_duration)
    motor2.spin(speed, ramp_type, ramp_duration)
    motor3.spin(speed/2, ramp_type, ramp_duration)
    motor4.spin(speed/2, ramp_type, ramp_duration)
  elif dir == "A": 
    motor1.spin(speed, ramp_type, ramp_duration)
    motor3.spin(speed/2, ramp_type, ramp_duration)
    motor4.spin(speed/2, ramp_type, ramp_duration)
  elif dir == "D": 
    motor2.spin(speed, ramp_type, ramp_duration)
    motor3.spin(speed/2, ramp_type, ramp_duration)
    motor4.spin(speed/2, ramp_type, ramp_duration)
  elif dir == "DOWN": 
    rm3.spin(speed, ramp_type, ramp_duration)
    rm4.spin(speed, ramp_type, ramp_duration)
  elif dir == "S": 
    rm1.spin(speed, ramp_type, ramp_duration)
    rm2.spin(speed, ramp_type, ramp_duration)
    motor3.spin(speed/2, ramp_type, ramp_duration)
    motor4.spin(speed/2, ramp_type, ramp_duration)
  else: 
    print("<< INVALID DIRECTION")
  time.sleep(duration)
  for motor in motors: 
    motor.stop()
  for rm in rev: 
    rm.stop()
    
def main():   
  # INITIALIZE GPIO, MOTORS, AND SENSORS
  # MOTOR 1 IS LEFT SIDE FORWARD FACING, MOTOR 2 IS RIGHT SIDE FORWARD FACING, MOTOR 3 IS DOWN, MOTOR 4 IS DOWN
  pi = pigpio.pi()
  Motor.init()
  accel = Accelerometer(0x68) # BMI270 default address
  gyro = Gyroscope(0x68) # BMI270 default address
  mag = Magnetometer(1, 0x14) # I2C Bus 1
  motorPins = [[21, 13], [20, 6], [16, 5], [19, 26]]
  motors, rev = [], []
  for i in range(4): 
    motors.append(Motor(motorPins[i][0], motorPins[i][1], pi))
    rev.append(Motor(motorPins[i][1], motorPins[i][0], pi))
  print("ENTERING BLIMP CONSOLE")
  print("""MENU: 
  RUN MOTOR >> R
  COLLECT DATA >> C
  LOG DATA >> L
  MENU >> M
  QUIT >> Q
  """)
  cmd = '!'
  while cmd != 'Q': 
    cmd = input("blimp-y7 INPUT >> ")
    if cmd == 'M': 
      print("""MENU: 
      RUN MOTOR >> R
      COLLECT DATA >> C
      LOG DATA >> L
      MENU >> M
      QUIT >> Q
      """)
    elif cmd == 'C': 
      collect_data(accel, gyro, mag)
    elif cmd == 'R': 
      direction = input("DIRECTION (UP, DOWN, W, A, S, D) >> ")
      move(motors, rev, direction)
    elif cmd == 'L': 
      log_data(accel, gyro, mag)      
    else: 
      print("<< INVALID COMMAND")
  print("<< CLEANING MOTOR GPIO RESOURCES...")
  # Clean up GPIO resources used by the motor
  for motor in motors: 
    motor.cleanup()
  print("<< EXITING BLIMP CONSOLE")
  
if __name__ == "__main__": 
  main()
