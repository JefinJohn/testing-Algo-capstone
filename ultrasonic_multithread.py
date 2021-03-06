import RPi.GPIO as GPIO
import time
import threading

distance =0;

def ultrasonic ():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(echoPIN,GPIO.IN)
    GPIO.setup(triggerPIN,GPIO.OUT)
    GPIO.setwarnings(True)
 while True:
     echoPIN = 15
     triggerPIN = 14

     global distance
     duration = 0
     GPIO.output(triggerPIN, 0)
     time.sleep(0.000002)
     GPIO.output(triggerPIN, 1)
     time.sleep(0.000010)
     GPIO.output(triggerPIN, 0)
     time.sleep(0.000002)
     # wait for echo reading
     while GPIO.input(echoPIN) == 0: pass
     startT = time.time()
     while GPIO.input(echoPIN) == 1: pass
     feedbackT = time.time()

     # calculating distance
     if feedbackT == startT:
      distance = "N/A"
     else:
      duration = feedbackT - startT
      soundSpeed = 34300 # cm/s
      distance = duration * soundSpeed / 2
      distance = round(distance, 1)
     time.sleep(0.2)
 
def main():
    global distance
    x=threading.Thread(target=ultrasonic)
    x.start()
    while(1):
        print("Sensor Reading:")
        print(distance)

if __name__ == "__main__":
    main()

