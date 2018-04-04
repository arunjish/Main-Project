import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

ML1= 14
ML2= 15

MR1= 23
MR2= 24

TRIG1 = 23
ECHO1 = 24

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)

GPIO.setup(ML1,GPIO.OUT)
GPIO.setup(ML2,GPIO.OUT)
GPIO.setup(MR1,GPIO.OUT)
GPIO.setup(MR2,GPIO.OUT)

def forward(delay):
	GPIO.output(ML1, True)
        GPIO.output(ML2, False)

        GPIO.output(MR1, True)
        GPIO.output(MR2, False)
	time.sleep(delay)
        print("forward")
def backward(delay):
	GPIO.output(ML2, True)
        GPIO.output(ML1, False)

        GPIO.output(MR2, True)
        GPIO.output(MR1, False)

	time.sleep(delay)
        print ("Backwords")

def left(delay):
        GPIO.output(ML1, True)
        GPIO.output(ML2, False)

        GPIO.output(MR1, False)
        GPIO.output(MR2, False)
	time.sleep(delay)
        print ("left")

def right(delay):
        GPIO.output(ML1, False)
        GPIO.output(ML2, False)

        GPIO.output(MR1, True)
        GPIO.output(MR2, False)

	time.sleep(delay)
        print ("right")

def stop(delay):
        GPIO.output(ML1, False)
        GPIO.output(ML2, False)

        GPIO.output(MR1, False)
        GPIO.output(MR2, False)
        print ("Stop")
	time.sleep(delay)

def diffLeft(delay):
	GPIO.output(ML1, True)
        GPIO.output(ML2, False)

        GPIO.output(MR1, False)
        GPIO.output(MR2, True)
        print ("\t diff---left")
	time.sleep(delay)

def diffRight(delay):
        GPIO.output(ML1, False)
        GPIO.output(ML2, True)

        GPIO.output(MR1, True)
        GPIO.output(MR2, False)
        print ("\t diff---Right")
        time.sleep(delay)


def follow_previous_direction(direction):
                        if direction=="r":
                                right(0)
                                time.sleep(0.05)
                                stop()
                        elif direction=="l":
                                left(0)
                                time.sleep(0.05)
                                stop()


def distance(triger,echo):
    # set Trigger to HIGH
    GPIO.output(triger, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(echo, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(echo) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(echo) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


def getDistances():
    d1=distance(TRIG1,ECHO1)
    d2=distance(TRIG1,ECHO1)
    d3=distance(TRIG1,ECHO1)
    return [d1,d2,d3]


#forward(1)
#stop(0)
