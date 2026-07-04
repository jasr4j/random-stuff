# Group Y7 Blimp Code

## INSTALL GUIDE: 
1. Download ZIP of this repository from [https://github.com/jasr4j/blimp](https://github.com/jasr4j/blimp)
2. Extract ZIP into a folder called "blimp"
3. Open the terminal and move the active directory using cd to the directory that contains the extracted blimp folder
4. Run ```scp -r blimp y7@y7.local:/home/y7/Desktop```

## TESTING GUIDE: 
1. Connect batteries to Raspberry Pi
2. Put Raspberry Pi into the gondola
3. Turn on the Falcon Flight Board
4. Plug in motors and camera
5. Steps 6-10 of QUICK START GUIDE
6. Mount the gondola that contains the Raspberry Pi running code onto the bottom of the balloon

## HARDWARE: 
1. Raspberry Pi Zero W
2. Falcon Flight Board (Credit: Eli Ferrara)
3. 2x 4V batteries
4. 4x Motors
5. Large Mylar (BoPET) Balloon filled with Helium
6. 3D Printed Gondola (Credit: Daisy Hu)

## CREATE VENV: 
1. ```python3 -m venv venv``` (Creates python3 virtual environment called venv in the current directory)

## CLOSE PI GUIDE: 
1. ```deactivate```
2. Ctrl+D

## SETUP WIFI AUTOCONNECT: 
```bash
nmcli radio wifi on
nmcli device wifi connect "YOUR_SSID" password "YOUR_PASSWORD"
nmcli connection show
nmcli connection modify "YOUR_SSID" connection.autoconnect yes
```

## QUICK START GUIDE: 
1. Plug in Raspberry Pi **AND** Falcon Flight Board
2. Make sure the green light is on for the Raspberry Pi
3. Autoconnect to Raspberry Pi to Hotspot and Laptop/PC to Hotspot
4. Turn on Falcon Flight Board and make sure the green light is on
5. Plug in motors and camera
6. ```ssh y7@y7.local``` (password: ```y7```)
7. ```cd ~/{code folder}```
8. ```source quickstart.sh``` (Starts PiGPIO Daemon and enters virtual environment)
9. ```which python3``` (Should output /home/y7/{code folder}/venv)
10. ```python3 main.py```

## DEPENDENCIES: 
1. Git: ```sudo apt install git```
2. Python3: ```sudo apt install python3```
3. Make: ```sudo apt install make```
5. Blimp-Utils: ```sudo curl -sSL https://raw.githubusercontent.com/Ballistyxx/blimp-utils/refs/heads/main/install.sh | sh```
6. PiGPIO: ```git clone https://github.com/joan2937/pigpio.git && cd pigpio && make && sudo make install && cd ..```
