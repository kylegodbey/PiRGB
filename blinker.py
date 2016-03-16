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
redRGB = int(raw_input("Red: "))
greenRGB = int(raw_input("Green: "))
blueRGB = int(raw_input("Blue: "))
reddc = int(round(100*redRGB/255.0))
greendc = int(round(100*greenRGB/255.0))
bluedc = int(round(100*blueRGB/255.0))
redpwm.start(reddc)
greenpwm.start(greendc)
bluepwm.start(bluedc)

print("Babby's First PWM")
try:
	while 1:
		if GPIO.input(buttonPin):
			redpwm.ChangeDutyCycle(reddc)
			greenpwm.ChangeDutyCycle(greendc)
			bluepwm.ChangeDutyCycle(bluedc)
		else:
			redpwm.ChangeDutyCycle(40)
			greenpwm.ChangeDutyCycle(70)
			bluepwm.ChangeDutyCycle(20)
			#time.sleep(0.075)
except KeyboardInterrupt:
	redpwm.stop()
	greenpwm.stop()
	bluepwm.stop()
	GPIO.cleanup()
