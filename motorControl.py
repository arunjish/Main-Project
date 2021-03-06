import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# ML1 = 7
# ML2 = 8
#
# MR1 = 23
# MR2 = 24

ML1 = 23
ML2 = 24

MR1 = 7
MR2 = 8

TRIG1 = 2
ECHO1 = 3

TRIG2 = 17
ECHO2 = 27

TRIG3 = 19
ECHO3 = 26

GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.setup(TRIG3, GPIO.OUT)
GPIO.setup(ECHO3, GPIO.IN)

GPIO.setup(ML1, GPIO.OUT)
GPIO.setup(ML2, GPIO.OUT)
GPIO.setup(MR1, GPIO.OUT)
GPIO.setup(MR2, GPIO.OUT)

def setPin():
    GPIO.setup(TRIG1, GPIO.OUT)
    GPIO.setup(ECHO1, GPIO.IN)
    GPIO.setup(TRIG2, GPIO.OUT)
    GPIO.setup(ECHO2, GPIO.IN)
    GPIO.setup(TRIG3, GPIO.OUT)
    GPIO.setup(ECHO3, GPIO.IN)

    GPIO.setup(ML1, GPIO.OUT)
    GPIO.setup(ML2, GPIO.OUT)
    GPIO.setup(MR1, GPIO.OUT)
    GPIO.setup(MR2, GPIO.OUT)




def forward(delay):
    GPIO.output(ML1, True)
    GPIO.output(ML2, False)

    GPIO.output(MR1, True)
    GPIO.output(MR2, False)
    print("forward")
    time.sleep(delay)


def backward(delay):
    GPIO.output(ML2, True)
    GPIO.output(ML1, False)

    GPIO.output(MR2, True)
    GPIO.output(MR1, False)

    print("Backwords")
    time.sleep(delay)


def left(delay):
    GPIO.output(ML1, True)
    GPIO.output(ML2, False)

    GPIO.output(MR1, False)
    GPIO.output(MR2, False)
    print("left")
    time.sleep(delay)


def right(delay):
    GPIO.output(ML1, False)
    GPIO.output(ML2, False)

    GPIO.output(MR1, True)
    GPIO.output(MR2, False)

    print("right")
    time.sleep(delay)


def stop(delay):
    GPIO.output(ML1, False)
    GPIO.output(ML2, False)

    GPIO.output(MR1, False)
    GPIO.output(MR2, False)
    print("Stop")
    time.sleep(delay)



def distance(triger, echo):
    # set Trigger to HIGH
    GPIO.output(triger, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    # GPIO.output(echo, False)

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
    d1 = myDistance(TRIG1, ECHO1)
    d2 = myDistance(TRIG2, ECHO2)
    d3 = myDistance(TRIG3, ECHO3)
    distances=[d1, d2, d3]
    print(distances)
    return distances


def myDistance(trigger,echo):
    GPIO.output(trigger, False)
    # print("Waiting For Sensor To Settle")
    # time.sleep(1)
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    while GPIO.input(echo) == 0:
        pulse_start = time.time()
    while GPIO.input(echo) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    # print(level)
    return int(distance)

#
# if __name__ == '__main__':
#     setPin()
#     distances = getDistances()
#     print(distances)

# forward(1)
# stop(0)
