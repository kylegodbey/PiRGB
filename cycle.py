import RPi.GPIO as GPIO
import time

#pins
redPin = 23
greenPin = 24
bluePin = 25
buttonPin = 17

reddc = 95 #duty cycle
greendc = 1 
bluedc = 1

GPIO.setmode(GPIO.BCM) # this uses the broadcom numbering
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

redpwm = GPIO.PWM(redPin, 50)
greenpwm = GPIO.PWM(greenPin, 50)
bluepwm = GPIO.PWM(bluePin, 50)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#starting states for pwm and led pin
redpwm.start(0)
greenpwm.start(0)
bluepwm.start(0)

counter = 0

print("Babby's First PWM")
try:
	while 1:
		if (counter % 600 < 100):
			redpwm.ChangeDutyCycle(100)
			greenpwm.ChangeDutyCycle(0)
			bluepwm.ChangeDutyCycle(counter % 100)
			counter = counter + 1
			time.sleep(.01)
		elif (counter % 600 < 200):
			redpwm.ChangeDutyCycle(100 - (counter % 100))
			greenpwm.ChangeDutyCycle(0)
			bluepwm.ChangeDutyCycle(100)
			counter = counter + 1
			time.sleep(.01)
		elif (counter % 600 < 300):
			redpwm.ChangeDutyCycle(0)
			greenpwm.ChangeDutyCycle(counter % 100)
			bluepwm.ChangeDutyCycle(100)
			counter = counter + 1
			time.sleep(.01)
		elif (counter % 600 < 400):
			redpwm.ChangeDutyCycle(0)
			greenpwm.ChangeDutyCycle(100)
			bluepwm.ChangeDutyCycle(100 - (counter % 100))
			counter = counter + 1
			time.sleep(.01)
		elif (counter % 600 < 500):
			redpwm.ChangeDutyCycle((counter % 100))
			greenpwm.ChangeDutyCycle(100)
			bluepwm.ChangeDutyCycle(0)
			counter = counter + 1
			time.sleep(.01)
		else:
			redpwm.ChangeDutyCycle(100)
			greenpwm.ChangeDutyCycle(100 - (counter % 100))
			bluepwm.ChangeDutyCycle(0)
			counter = counter + 1
			time.sleep(.04)
except KeyboardInterrupt:
	redpwm.stop()
	greenpwm.stop()
	bluepwm.stop()
	GPIO.cleanup()
