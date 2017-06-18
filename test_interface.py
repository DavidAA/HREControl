import CHIP_IO.GPIO as GPIO

GPIO.setup("XIO-P0", GPIO.OUT)

while True:
        key_input = raw_input()
        if key_input.lower() == "on":
                print 'Setting to "on"'
                GPIO.output("XIO-P0", GPIO.HIGH)
                print 'On'
        elif key_input.lower() == "off":
                print 'Setting to "off"'
                GPIO.output("XIO-P0", GPIO.LOW)
                print 'Off'
        else:
                print "Not recognized. Please enter 'on' or 'off'"

GPIO.cleanup()
