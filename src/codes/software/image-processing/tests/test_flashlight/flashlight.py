import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM) 
GPIO.setup(4, GPIO.OUT) 

GPIO.output(4, GPIO.LOW)
time.sleep(1)
GPIO.output(4, GPIO.HIGH)
GPIO.output(4,GPIO.LOW)
GPIO.cleanup()


