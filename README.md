# flashLedDisplay
Minimalist temperature display by flashing one LED. </br>
By flashing a LED, one can display 2 digit temperatures effectively.
The user counts the long flashes for tens, and the short dashes for ones.
e.g. 26 degrees is dash dash dit dit dit dit dit dit  </br>
This Raspberry Pi (RPI) python program reads a Dallas DS18B20 temperature sensor and makes its value known by flashing an LED.
For those with poor eyesight like me without my eyeglasses on,  it works well from across the room.  </br>
First read https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20  </br>
If you are not using  GPIO 21 for the LED, then adjust the value of LED = 21 to the GPIO number you are using

Here is the debug output for the outside sensor reading 19687 raw (1.9687 Celsius) . Each line is a flash of the LED

firstloop for tens digit. i= 10000</br>
</br>
Secondloop for ones digit. i= 9687 </br>
Secondloop for ones digit. i= 8687 </br>
Secondloop for ones digit. i= 7687 </br>
Secondloop for ones digit. i= 6687 </br>
Secondloop for ones digit. i= 5687 </br>
Secondloop for ones digit. i= 4687 </br>
Secondloop for ones digit. i= 3687 </br>
Secondloop for ones digit. i= 2687 </br>
Secondloop for ones digit. i= 1687 </br>
</br>
 2023 6 11 , 18 : 24   inside= 24437 outside= 19687 


