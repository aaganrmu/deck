# How to setup the whole thing

## Get GIT

1. Install: `sudo apt-get install git`

## Upgrade shell to zsh

1. Install: `sudo apt-get install zsh`
2. Make default: `chsh -s /bin/zsh`
3. Install oh-my-zsh: `sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`

## Setup main display (1024x600)
1. Edit config `sudo nano /boot/config.txt`
2. add/uncomment `disable_overscan=1
hdmi_cvt=1024 600 60 3 0 0 0
hdmi_group=2
hdmi_mode=87`

## Setup OLED display (SH1106)

1. Install python3 packages `sudo apt-get install python3-dev python3-pip python3-pil python3-smbus` (using sudo because we're running from systemd later)
2. Edit config `sudo nano /boot/config.txt`
3. add/uncomment `dtparam=i2c_arm=on
` 
4. add `dtparam=i2c_baudrate=1000000`
5. Reboot

## Enable deck-hardware service
Note that there's multiple services
1. Make sure deck-hardware.service points to the correct deck-hardware-service.py
2. Give the python file execute rights: `sudo chmod +x deck-hardware-service.py`
3. Copy the file to systemd folder: `sudo cp deck-hardware.service /etc/systemd/system/`
4. Give it the correct rights: `sudo chmod 644 /etc/systemd/system/deck-hardware.service`
5. Reload services: `sudo systemctl daemon-reload`
6. Start service (to test): `sudo systemctl start deck-hardware.service`
7. Check status: `sudo systemctl status deck-hardware.service`
8. Enable automatic startup: `sudo systemctl enable deck-hardware.service`

## Add scripts folder to $PATH
Add to .zshrc:
export $PATH=/home/pi/git/deck/scripts:$PATH

## Random stuff

Mount remote folder through SSH: `sudo sshfs -o allow_other,default_permissions,IdentityFile=/home/elmarw/.ssh/id_rsa pi@192.168.2.100:/ /mnt/rpi`
Add `logo.nologo` to /boot/cmdline.txt to remove the 4 raspberries from the top of the screen
