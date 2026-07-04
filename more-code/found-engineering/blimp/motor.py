import sys
import tty
import termios
import time
import pigpio

# --- PIN CONFIGURATION ---
# Matching your original setup: [Forward/Positive Pin, Reverse/Negative Pin]
MOTOR_PINS = {
    1: [21, 13],  # Motor 1: Left Front
    2: [20, 6],   # Motor 2: Right Front
    3: [16, 5],   # Motor 3: Down/Up Left
    4: [19, 26]   # Motor 4: Down/Up Right
}

REV_PINS = {
    1: [13, 21],  # Motor 1: Left Front
    2: [6, 20],   # Motor 2: Right Front
    3: [5, 16],   # Motor 3: Down/Up Left
    4: [26, 19]   # Motor 4: Down/Up Right
}

SPEED = 75       # Motor speed (0 to 255)
PWM_FREQ = 1000   # 1kHz frequency is standard for DC motors

# Initialize pigpio
pi = pigpio.pi()
if not pi.connected:
    print("CRITICAL: pigpiod daemon not running! Run 'sudo pigpiod' first.")
    sys.exit(1)

# Initialize all motor pins as outputs
for pins in MOTOR_PINS.values():
    pi.set_mode(pins[0], pigpio.OUTPUT)
    pi.set_mode(pins[1], pigpio.OUTPUT)

def set_motor(motor_num, target_speed, direction="FORWARD"):
    """Controls a single motor's speed and direction."""
    pin_a, pin_b = MOTOR_PINS[motor_num]
    
    if target_speed == 0:
        pi.write(pin_a, 0)
        pi.write(pin_b, 0)
    elif direction == "FORWARD":
        pi.set_PWM_frequency(pin_a, PWM_FREQ)
        pi.set_PWM_dutycycle(pin_a, target_speed)
        pi.write(pin_b, 0)
    elif direction == "REVERSE":
        pi.write(pin_a, 0)
        pi.set_PWM_frequency(pin_b, PWM_FREQ)
        pi.set_PWM_dutycycle(pin_b, target_speed)

def stop_all_motors():
    """Safety stop for all attached motors."""
    for i in range(1, 5):
        set_motor(i, 0)

def get_keypress():
    """Reads a single keypress from the terminal without needing 'Enter'."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSANOW, old_settings)
    return ch.upper()

def print_menu():
    print("\r" + "="*45)
    print("\r      BLIMP FLIGHT CONTROL CONSOLE           ")
    print("\r" + "="*45)
    print("\r  [W] Forward    [Q] Ascend (Up)           ")
    print("\r  [A] Left       [E] Descend (Down)        ")
    print("\r  [S] Backward                             ")
    print("\r  [D] Right                                ")
    print("\r                                           ")
    print("\r  [SPACE] Emergency Stop                   ")
    print("\r  [X] Exit Controller                      ")
    print("\r" + "="*45)

def main():
    try:
        stop_all_motors()
        print_menu()
        
        while True:
            sys.stdout.write("\rFlight Status: IDLE | Awaiting command... ")
            sys.stdout.flush()
            
            key = get_keypress()
            
            if key == 'X':
                print("\r\nExiting control interface...")
                break
                
            elif key == ' ':
                stop_all_motors()
                print("\rFlight Status: EMERGENCY STOP ENFORCED          ", end="")
                time.sleep(0.5)
                
            elif key == 'W':
                print("\rFlight Status: MOVING FORWARD                     ", end="")
                set_motor(1, SPEED, "FORWARD")
                set_motor(2, SPEED, "FORWARD")
                set_motor(3, SPEED // 2, "FORWARD")
                set_motor(4, SPEED // 2, "FORWARD")
                
            elif key == 'S':
                print("\rFlight Status: MOVING BACKWARD                    ", end="")
                set_motor(1, SPEED, "REVERSE")
                set_motor(2, SPEED, "REVERSE")
                set_motor(3, SPEED // 2, "FORWARD")
                set_motor(4, SPEED // 2, "FORWARD")
                
            elif key == 'A':
                print("\rFlight Status: TURNING LEFT                       ", end="")
                set_motor(2, SPEED, "FORWARD") # Push right side forward to pivot left
                set_motor(1, 0)
                
            elif key == 'D':
                print("\rFlight Status: TURNING RIGHT                      ", end="")
                set_motor(1, SPEED, "FORWARD") # Push left side forward to pivot right
                set_motor(2, 0)
                
            elif key == 'Q':
                print("\rFlight Status: ASCENDING (UP)                     ", end="")
                set_motor(3, SPEED, "FORWARD")
                set_motor(4, SPEED, "FORWARD")
                
            elif key == 'E':
                print("\rFlight Status: DESCENDING (DOWN)                  ", end="")
                set_motor(3, SPEED, "REVERSE")
                set_motor(4, SPEED, "REVERSE")
                
            # Keep motors engaged briefly unless holding down a key loops it
            time.sleep(0.3)

    except KeyboardInterrupt:
        print("\nSession interrupted.")
    finally:
        print("\nShutting down motors and cleaning up GPIO pins...")
        stop_all_motors()
        pi.stop()

if __name__ == '__main__':
    main()

