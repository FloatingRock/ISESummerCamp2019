# Projects

## Level 0: Test environment
* [Example 0: Hello World](examples/0_hello_world/README.md)

## Level 1: Test inventory
* Program actuators
  * [Example 1: Light an LED](examples/1_light_led/README.md)
* Read sensor values and print to terminal
  * [Example 2: Read light sensor](examples/2_read_light/README.md)
  * [Example 3: Read a Potentiometer](examples/3_read_potentiometer/README.md)

## Level 2: Combine sensor-actuator
* Read sensor value and conditionally activate actuator
  * [Example 4: Build a Nightlight](examples/4_build_nightlight/README.md)
  * [Example 5: Dim the Nightlight](examples/5_dim_nightlight/README.md)

## Level 3: Pulse-width modulation (PWM)
* [Example 6: Make noise with a buzzer](examples/6_buzzer_noise/README.md)
* [Example 7: Introduce pulse-width modulation (PWM)](examples/7_intro_pwm/README.md)
* [Example 8: Play a sound sequence](examples/8_play_sound/README.md)
* [Example 9: Explore the sound of sensors](examples/9_sensor_sound/README.md)

## Level 4: Bring it all together
* [Simple Theremin](examples/simple_theremin/README.md)

## Level 5: Advanced
* Parse midi file into PWM (frequency, duration) tuples


# Documentation

## Connect via SSH

1. Enable SSH
    1. Open the Raspberry Pi Software Configuration Tool (`raspi-config`):
    ``` bash
    $ sudo raspi-config
    ```
    2. 5 Interfacing Options -> P2 SSH
2. Connect to a wlan network and report its assigned IP:
    ``` bash
    $ ip addr show wlan0
    ```
3. Use an SSH client to connect:
    * On Linux: `ssh`
    * On Windows: [PuTTY](https://www.putty.org/)

## RPi.GPIO
``` bash
$ wget -O - https://raspi.tv/download/rpigpio.txt
```

## PWM
https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/

## Useful tools

### `gpio`

* List all GPIO pins along with their `BOARD` and `BCM` numbers:
``` bash
$ gpio readall
```

* Set the mode of a pin to either `input`, `output`, or `pwm`:
``` bash
$ gpio mode <pin> <mode>
```

* Digital read/write:
``` bash
$ gpio read <pin>
$ gpio write <pin> <value>
```

* Analog read/write:
``` bash
$ aread <pin>
$ awrite <pin> <value>
```

* Write a byte to the main 8 GPIO pins:
``` bash
$ wb <value>
```

* Toggle or blink a given pin:
``` bash
$ toggle <pin>
$ blink <pin>
```

* Set the clock frequency of a given `output` pin:
``` bash
$ clock <pin> <frequency>
```

* Write a PWM value (0-1023) to a given `pwm` pin:
``` bash
$ pwm <pin> <value>
```


# Inventory

| Actuator | Sensor | Compute |
|----------|--------|---------|
| Audio:<ul><li>Piezo buzzer</li><li>Dayton</li></ul> | Infrared Reflective<br><i>line follow</i> | Potentiometer |
| LED:<ul><li>5 red</li><li>5 green</li><li>5 yellow</li> | Cds photocell | Integrated Circuit: NAND |
