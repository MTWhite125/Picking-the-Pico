from machine import Pin, ADC 
import time 

led = Pin(0, Pin.OUT) 

# Potentiometer on ADC0 (GPIO26) 
pot = ADC(26) 

# Blink range (seconds) 
MIN_DELAY = 2   # fastest blink, 2 seconds 
MAX_DELAY = 6   # slowest blink, 6 seconds 

while True: 
    adc_value = pot.read_u16()   
    delay = MIN_DELAY + (adc_value / 65535) * (MAX_DELAY - MIN_DELAY) 
    led.toggle() 
    time.sleep(delay) 