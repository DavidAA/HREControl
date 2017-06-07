from bottle import route, run
import CHIP_IO.GPIO as GPIO
import getIP

GPIO.setup("XIO-P0", GPIO.OUT)
GPIO.output("XIO-P0", GPIO.HIGH)

@route('/')
def index():
	GPIO.output("XIO-P0", GPIO.HIGH)
        return "<a href='/on' style='text-decoration: none'><div style='background-color: red; height: 100px; width: 100px; border-radius: 100%'><p style='color: white; font-weight: 900; text-align: center; vertical-align: middle; line-height: 100px; font-size: 260%; margin: 0px'>ON</p></div></a>"

@route('/on')
def on():
	GPIO.output("XIO-P0", GPIO.LOW)
	return "<a href='/' style='text-decoration: none'><div style='background-color: red; height: 100px; width: 100px; border-radius: 100%'><p style='color: white; font-weight: 900; text-align: center; vertical-align: middle; line-height: 100px; font-size: 260%; margin: 0px'>OFF</p></div></a>"

ip_addr = getIP.getIP()

run(host=ip_addr, port=8000, debug=True)

GPIO.cleanup()
