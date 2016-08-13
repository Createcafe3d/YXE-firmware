# Build Instructions

## Get the working compiler instructions for linux (debians)
This has been tried on rasbian, ubuntu 14.04, 16.04
* Note: This will remove the any stale version of the compiler you may have
```shell
sudo add-apt-repository ppa:terry.guo/gcc-arm-embedded
sudo apt-get remove binutils-arm-none-eabi gcc-arm-none-eabi
```
__It will probably just say 0 removed if you didn't have it installed.__

Now install the compiler :)
```shell
sudo apt-get update
sudo apt-get install gcc-arm-none-eabi
```
"UNDO" commands for the above (Don't run this unless something broke for you)
```shell
sudo add-apt-repository --remove ppa:terry.guo/gcc-arm-embedded
sudo apt-get update
sudo apt-get install binutils-arm-none-eabi gcc-arm-none-eabi
```
## Clone and make make the firmware bin file :)
```shell
git clone git@github.com:Createcafe3d/YXE-firmware.git
cd YXE-firmware
make
```
This should result in a main.bin in the local directory

## Get the source for dfu-util (firmware flashing tool)
Not needed, you can use the static ones we've given "./standalone_dfu/"
```shell
git clone git://git.code.sf.net/p/dfu-util/dfu-util
cd dfu-util
./autogen.sh
./configure
sudo make install
```
Now you can flash firmware with the following command:
```shell
Linux:
dfu-util -a 0 --dfuse-address 0x08000000 -D main.bin -d 16d0:0af3

Windows:
run standalone_dfu/windows/wind_dfu.bat with main.bin in the same directory
```
## Get openocd (linux - Only needed for use with debug board)
```shell
sudo apt-get remove openocd
git clone git://git.code.sf.net/p/openocd/code openocd-code
cd openocd-code
./bootstrap
./configure
make
sudo make install
```
Discovery board and YXE3D pinout to help connecting up stuff:
```shell
Discovery board (reading SWD) : [o,NRST,SDIO,GND,SDCLK,o]
YXE3D (boards 1.13 and older):  [o,NRST,GND;o,SDCLK,SDIO]
-diagram drawn with USB on the left
```
Use openocd to connect the stmf4discovery gdb debug to localhost:3333
```shell
sudo openocd -f stlink.cfg
```
Run the gdb terminal and connect to our opencd debug port
```shell
arm-none-eabi-gdb main.elf
(gdb) target remote localhost:3333
```
Example Commands:
* monitor reset halt - stop the microcontroller
* c - continue
* break file.c:32 - break on line 32 in file.c

#What's still missing/not working
* Optimisations above -O0 will fail to boot the chip 
* SD card/standalone library
    * Needed "toolchain":
        1. gcode through calibrated transform (in YXEtools) into deflection points (python?)
        2. Write deflection and some semblence of framing per layer to help drip counts (python?) to file
        3. Make the firmware read above file, and figure out it's own go|no-go|skip-layer decision
    * Even Further using the I2C or SPI with CS, we can add in an screen for an all in one.
* Angular Acceleration
    * Most fdm printers accelerate and decelerate their movement in firmware
    * This is usually done by buffering a few commands and calculating intermediate steps
    * ... but the units are in % of deflection as 18bit numbers and angular acceleration.
    * I will give a printer and a bunch of resin to anyone who solves this problem (with working code)
        * Well, before I get to it

