import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 18
ECHO = 24
buzzer = 3
led = 2
counter = 0

print(" Distance Measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)



while True:
    GPIO.output(TRIG, False)

    time.sleep(.5)

    GPIO.output(TRIG, True)
    time.sleep(0.01)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start=time.time()

    while GPIO.input(ECHO)==1:
        pulse_end=time.time()

    pulse_duration=pulse_end-pulse_start

    distance = pulse_duration*11150
    distance = round(distance,2)

    if counter>=15:
        print("*******INTRUDER ALERT!!!*******")
        GPIO.output(led, GPIO.HIGH)
        GPIO.output(buzzer, GPIO.LOW)
        time.sleep(10)
        counter = 0
    else:
        if distance < 80:
            GPIO.output(buzzer, GPIO.LOW)
            print("Object detected. Warning! Alarm will sound for 10 seconds, if it continues.")
            GPIO.output(led, GPIO.HIGH)
            counter = counter + 1
        else:
            GPIO.output(buzzer, GPIO.HIGH)
            GPIO.output(led, GPIO.LOW)
            print("No intruders: BUZZER OFF/LED ON")
