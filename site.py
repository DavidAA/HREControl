from bottle import route, run, template, static_file
#import CHIP_IO.GPIO as GPIO
import getIP

#GPIO.setup("XIO-P0", GPIO.OUT)
#GPIO.output("XIO-P0", GPIO.HIGH)

@route('/')
def index():
#	GPIO.output("XIO-P0", GPIO.HIGH)
#	return static_file('/views/index_style.css')
        return template('index.tpl')

@route('/static/<filename>')
def static(filename):
#	GPIO.output("XIO-P0", GPIO.HIGH)
#	return static_file('/views/index_style.css')
        return static_file(filename, root='static')

ip_addr = getIP.getIP()

run(host=ip_addr, port=8000, debug=True)

#GPIO.cleanup()
