# How to setup the whole thing

## Install pip & add to path:

1. `sudo apt-get install python3-distutils`
2. `python3 get-pip.py`
3. Add `export PATH="$PATH:/home/pi/.local/bin"` to `~/.bash_profile`

## Setup OLED display

1. Install python3 packages `sudo apt-get install python3-dev python3-pip python3-pil`
2. Edit config `sudo nano /boot/config.txt`
3. add/uncomment `dtparam=i2c_arm=on
` 
4. add `dtparam=i2c_baudrate=1000000`
5. Reboot
6. Go to `Adafruit_Python_SSD1306` folder
7. Install using `sudo python3 setup.py install`

## Enable deck-hardware service

1. Make sure deck-hardware.service points to the correct deck-hardware-service.py
2. Copy the file to systemd folder: `sudo cp deck-hardware.service /etc/systemd/system/`
3. Reload services: `sudo systemctl daemon-reload`
4. Start service (to test): `sudo systemctl start deck-hardware.service`
5. Check status: `sudo systemctl status deck-hardware.service`
6. Enable automatic startup: `sudo systemctl enable deck-hardware.service`