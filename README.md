# OrangePi Zero MMDVM Fan Controller

An OrangePi Zero MMDVM fan controll service based on [wiringOP](https://github.com/orangepi-xunlong/wiringOP) . Tested on OrangePi Zero with [Pi-Star](https://www.pistar.uk/).

The fan control pin is physical pin 12 （PA07）.

## Install Instructions

1. Build and install [wiringOP](https://github.com/orangepi-xunlong/wiringOP).

   ```
   rpi-rw
   cd ~
   git clone https://github.com/orangepi-xunlong/wiringOP.git
   cd wiringOP
   chmod 777 build
   ./build
   ```

   

2. OrangePi MMDVM Fan Controller install.

   ```bash
   rpi-rw
   cd ~
   git clone https://github.com/leonfg/opizero_fan_ctrl.git
   cd opizero_fan_ctrl
   sudo cp fan.service /etc/systemd/system
   sudo cp fan_thermal_ctl.py /boot
   sudo systemctl start fan
   sudo systemctl status fan
   sudo systemctl enable fan
   ```

3. Test.

   - Fan on test.

       ```bash
       python fan_on.py
       ```

   - Fan off test.

       ```
       python fan_off.py
       ```
   
       
   